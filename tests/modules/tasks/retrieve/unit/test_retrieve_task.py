import pytest

from meiga import Success, Failure
from unittest.mock import Mock

from meiga.assertions import assert_success, assert_failure

from taskmanager.src.modules.tasks.application.retrieve.retrieve_task import (
    RetrieveTask,
)
from taskmanager.src.modules.tasks.domain.errors import TaskNotFoundError
from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)


@pytest.mark.unit
def test_should_retrieve_task_happy_path(given_any_task_id, given_any_task):

    mock_task_repository = Mock(spec=ITaskRepository)
    mock_task_repository.retrieve = Mock(return_value=Success(given_any_task))

    use_case = RetrieveTask(mock_task_repository)

    result = use_case.execute(given_any_task_id)

    mock_task_repository.retrieve.assert_called_once()

    assert_success(result)


def test_should_return_task_not_found_error(given_any_task_id, given_any_task):

    mock_task_repository = Mock(spec=ITaskRepository)
    mock_task_repository.retrieve = Mock(
        return_value=Failure(TaskNotFoundError(given_any_task_id))
    )

    use_case = RetrieveTask(mock_task_repository)

    result = use_case.execute(given_any_task_id)

    mock_task_repository.retrieve.assert_called_once()

    assert_failure(result, value_is_instance_of=TaskNotFoundError)
