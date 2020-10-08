import json

import pytest


@pytest.mark.acceptance
def test_should_return_a_200_when_get_task(
    petisco_client_flask_app, given_any_title, given_any_description
):

    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title.value, "description": given_any_description.value}
    response = petisco_client_flask_app.post(
        "/taskmanager/task", data=json.dumps(data), headers=headers
    )
    assert response.status_code == 200

    task_id = response.json["task_id"]

    response = petisco_client_flask_app.get(f"/taskmanager/task/{task_id}")

    assert response.status_code == 200
    assert response.json["task"]["task_id"] == task_id
    assert response.json["task"]["title"] == given_any_title.value
    assert response.json["task"]["description"] == given_any_description.value
    assert "created_at" in response.json["task"]


@pytest.mark.acceptance
def test_should_return_a_404_when_get_task_of_non_existent_task(
    petisco_client_flask_app, given_any_task_id
):

    response = petisco_client_flask_app.get(
        f"/taskmanager/task/{given_any_task_id.value}"
    )

    assert response.status_code == 404
    assert response.json == {
        "error": {"message": "Task not found", "type": "TaskNotFoundError"}
    }


@pytest.mark.acceptance
def test_should_return_a_400_when_get_task_with_invalid_task_id(
    petisco_client_flask_app, given_any_task_id
):

    response = petisco_client_flask_app.get("/taskmanager/task/invalid_task_id")

    assert response.status_code == 400
    assert response.json == {
        "error": {
            "message": "Invalid TaskId. TaskId must be a valid 36-char UUID",
            "type": "InvalidTaskIdError",
        }
    }
