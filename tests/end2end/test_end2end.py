import os

import pytest
import requests


@pytest.fixture
def base_url(variables):
    return variables["host"]


@pytest.mark.end2end
@pytest.mark.skipif(
    not os.environ.get("END2END_TEST"),
    reason="To run end2end test, please define END2END_TEST envar",
)
def test_end2end(base_url, given_any_title, given_any_description):
    response = requests.get(f"{base_url}/healthcheck")
    assert response.status_code == 200

    response = requests.get(f"{base_url}/task/invalid_id")
    assert response.status_code == 404

    data = {"title": given_any_title, "description": given_any_description}
    response = requests.post(f"{base_url}/task", json=data)
    assert response.status_code == 200
    task_id = response.json()["task_id"]

    response = requests.get(f"{base_url}/task/{task_id}")
    assert response.status_code == 200
