import json

import pytest


@pytest.mark.acceptance
def test_should_return_a_200_when_post_task(
    client, database, given_any_title, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title, "description": given_any_description}
    response = client.post("/taskmanager/task", data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    assert "task_id" in response.json
    assert len(response.json["task_id"]) == 16
    assert response.json["message"] == "Created Task"


@pytest.mark.acceptance
def test_should_return_a_405_when_post_task_with_no_data(
    client, database, given_any_title, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {}
    response = client.post("/taskmanager/task", data=json.dumps(data), headers=headers)

    assert response.status_code == 400


@pytest.mark.acceptance
def test_should_return_a_400_when_post_task_with_no_title(
    client, database, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"description": given_any_description}
    response = client.post("/taskmanager/task", data=json.dumps(data), headers=headers)

    assert response.status_code == 400


@pytest.mark.acceptance
def test_should_return_a_400_when_post_task_with_no_description(
    client, given_any_title
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title}
    response = client.post("/taskmanager/task", data=json.dumps(data), headers=headers)

    assert response.status_code == 400


@pytest.mark.acceptance
def test_should_return_a_405_when_post_task_with_title_exceeds_length(
    client, given_any_title, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title * 20, "description": given_any_description}
    response = client.post("/taskmanager/task", data=json.dumps(data), headers=headers)
    assert response.status_code == 405
    assert response.json == {
        "error": {
            "message": "Exceed Length Limit",
            "type": "ExceedLengthLimitInputError",
        }
    }


@pytest.mark.acceptance
def test_should_return_a_405_when_post_task_with_description_exceeds_length(
    client, given_any_title, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title, "description": given_any_description * 200}
    response = client.post("/taskmanager/task", data=json.dumps(data), headers=headers)
    assert response.status_code == 405
    assert response.json == {
        "error": {
            "message": "Exceed Length Limit",
            "type": "ExceedLengthLimitInputError",
        }
    }
