import json

import pytest


@pytest.mark.acceptance
def test_should_return_a_200_when_delete_task(
    petisco_client_flask_app, given_any_title, given_any_description
):

    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title.value, "description": given_any_description.value}
    response = petisco_client_flask_app.post(
        "/taskmanager/task", data=json.dumps(data), headers=headers
    )

    task_id = response.json["task_id"]

    response = petisco_client_flask_app.delete(f"/taskmanager/task/{task_id}")

    assert response.status_code == 200


@pytest.mark.acceptance
def test_should_return_a_404_when_delete_task_of_non_existent_task(
    petisco_client_flask_app, given_any_task_id
):

    response = petisco_client_flask_app.delete(
        f"/taskmanager/task/{given_any_task_id.value}"
    )

    assert response.status_code == 404
    assert response.json == {
        "error": {"message": "Task not found", "type": "TaskNotFoundError"}
    }
