import pytest

from meiga import isSuccess, Failure
from unittest.mock import Mock

from meiga.assertions import assert_success, assert_failure
from petisco.events.interface_event_manager import IEventManager

from taskmanager.src.modules.tasks.application.create.create_task import CreateTask
from taskmanager.src.modules.tasks.domain.errors import TaskAlreadyExistError
from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)


@pytest.mark.unit
def test_should_create_task_happy_path(
    given_any_task_id, given_any_title, given_any_description
):

    mock_task_repository = Mock(spec=ITaskRepository)
    mock_task_repository.save = Mock(return_value=isSuccess)
    mock_event_manager = Mock(spec=IEventManager)
    mock_event_manager.publish_list = Mock(return_value=isSuccess)

    use_case = CreateTask(mock_task_repository, mock_event_manager)

    result = use_case.execute(given_any_task_id, given_any_title, given_any_description)

    mock_task_repository.save.assert_called_once()
    mock_event_manager.publish_list.assert_called_once()

    assert_success(result)


def test_should_return_task_already_exist_error(
    given_any_task_id, given_any_title, given_any_description
):

    mock_task_repository = Mock(spec=ITaskRepository)
    mock_task_repository.save = Mock(
        return_value=Failure(TaskAlreadyExistError(given_any_task_id))
    )
    mock_event_manager = Mock(spec=IEventManager)

    use_case = CreateTask(mock_task_repository, mock_event_manager)

    result = use_case.execute(given_any_task_id, given_any_title, given_any_description)

    mock_task_repository.save.assert_called_once()
    mock_event_manager.publish_list.assert_not_called()

    assert_failure(result, value_is_instance_of=TaskAlreadyExistError)
