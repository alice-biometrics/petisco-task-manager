import json
import pytest


@pytest.mark.acceptance
def test_should_return_a_200_when_post_task(
    petisco_client_flask_app, given_any_title, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title.value, "description": given_any_description.value}
    response = petisco_client_flask_app.post(
        "/taskmanager/task", data=json.dumps(data), headers=headers
    )
    assert response.status_code == 200
    assert "task_id" in response.json
    assert len(response.json["task_id"]) == 36
    assert response.json["message"] == "Created Task"


@pytest.mark.acceptance
def test_should_return_a_405_when_post_task_with_no_data(
    petisco_client_flask_app, given_any_title, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {}
    response = petisco_client_flask_app.post(
        "/taskmanager/task", data=json.dumps(data), headers=headers
    )

    assert response.status_code == 400


@pytest.mark.acceptance
def test_should_return_a_400_when_post_task_with_no_title(
    petisco_client_flask_app, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"description": given_any_description.value}
    response = petisco_client_flask_app.post(
        "/taskmanager/task", data=json.dumps(data), headers=headers
    )

    assert response.status_code == 400


@pytest.mark.acceptance
def test_should_return_a_400_when_post_task_with_no_description(
    petisco_client_flask_app, given_any_title
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {"title": given_any_title.value}
    response = petisco_client_flask_app.post(
        "/taskmanager/task", data=json.dumps(data), headers=headers
    )

    assert response.status_code == 400


@pytest.mark.acceptance
def test_should_return_a_405_when_post_task_with_title_exceeds_length(
    petisco_client_flask_app, given_any_title, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {
        "title": given_any_title.value * 20,
        "description": given_any_description.value,
    }
    response = petisco_client_flask_app.post(
        "/taskmanager/task", data=json.dumps(data), headers=headers
    )
    assert response.status_code == 405
    assert response.json == {
        "error": {
            "message": "Exceed Length Limit",
            "type": "ExceedLengthLimitInputError",
        }
    }


@pytest.mark.acceptance
def test_should_return_a_405_when_post_task_with_description_exceeds_length(
    petisco_client_flask_app, given_any_title, given_any_description
):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    data = {
        "title": given_any_title.value,
        "description": given_any_description.value * 200,
    }
    response = petisco_client_flask_app.post(
        "/taskmanager/task", data=json.dumps(data), headers=headers
    )
    assert response.status_code == 405
    assert response.json == {
        "error": {
            "message": "Exceed Length Limit",
            "type": "ExceedLengthLimitInputError",
        }
    }
