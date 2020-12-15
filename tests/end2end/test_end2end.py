import os
from time import sleep

import pytest
import requests
from petisco import Event


@pytest.fixture
def base_url(variables):
    return variables["host"]


def wait_for_event():
    sleep(1.0)


@pytest.mark.end2end
@pytest.mark.skipif(
    not os.environ.get("END2END_TEST"),
    reason="To run end2end test, please define END2END_TEST envar",
)
def test_end2end(base_url, given_any_task_id, given_any_title, given_any_description):

    response = requests.get(f"{base_url}/healthcheck")
    assert response.status_code == 200

    response = requests.get(f"{base_url}/task/invalid_id")
    assert response.status_code == 400

    response = requests.get(f"{base_url}/task/{given_any_task_id.value}")
    assert response.status_code == 404

    data = {"title": given_any_title.value, "description": given_any_description.value}
    response = requests.post(f"{base_url}/task", json=data)
    assert response.status_code == 200
    task_id = response.json()["task_id"]

    assert_task_count_is_equal_to(1, base_url)

    response = requests.get(f"{base_url}/task/{task_id}")
    assert response.status_code == 200
    data_to_delete = {"title": "Deleteme", "description": "Deleteme"}
    response = requests.post(f"{base_url}/task", json=data_to_delete)
    assert response.status_code == 200
    task_id_to_delete = response.json()["task_id"]

    assert_task_count_is_equal_to(2, base_url)

    response = requests.delete(f"{base_url}/task/{task_id_to_delete}")
    assert response.status_code == 200

    assert_task_count_is_equal_to(1, base_url)

    assert_recorded_events(base_url)


def assert_recorded_events(base_url):
    wait_for_event()

    response_events = requests.get(f"{base_url}/events")
    assert response_events.status_code == 200
    events = response_events.json().get("events")
    event_names = [Event.from_dict(event).event_name for event in events]

    expected_event_names = [
        "service.deployed",
        "task.created",
        "task.retrieved",
        "task.created",
        "task.removed",
    ]
    assert sorted(expected_event_names) == sorted(event_names)


def assert_task_count_is_equal_to(tasks_count: int, base_url: str):
    wait_for_event()
    response = requests.get(f"{base_url}/tasks/count")
    assert response.status_code == 200
    assert response.json() == {"tasks_count": tasks_count}
