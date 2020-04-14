import json

import pytest


@pytest.mark.acceptance
def test_should_return_a_200_with_task_info_when_get_task(
    client, given_any_title, given_any_description
):
    pass
    """ 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {"title": given_any_title, "description": given_any_description}
    response = client.post(
        "/taskmanager/task",
        data=json.dumps(data),
        headers=headers,
    )

    task_id = response.json["task_id"]

    response = client.get(
        "/taskmanager/task",
    )

    assert response.status_code == 200
    """
