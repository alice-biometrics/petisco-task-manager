import json

import pytest


@pytest.mark.acceptance
def test_should_return_a_200_when_get_task(
    client, database, given_any_title, given_any_description
):

    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title, "description": given_any_description}
    response = client.post("/taskmanager/task", data=json.dumps(data), headers=headers)

    task_id = response.json["task_id"]

    response = client.get(f"/taskmanager/task/{task_id}")

    assert response.status_code == 200
    assert response.json["task"]["task_id"] == task_id
    assert response.json["task"]["title"] == given_any_title
    assert response.json["task"]["description"] == given_any_description
    assert "created_at" in response.json["task"]


@pytest.mark.acceptance
def test_should_return_a_404_when_get_task_of_non_existent_task(
    client, database, given_any_task_id
):

    response = client.get(f"/taskmanager/task/{given_any_task_id}")

    assert response.status_code == 404
    assert response.json == {
        "error": {"message": "Task not found", "type": "TaskNotFoundHttpError"}
    }
