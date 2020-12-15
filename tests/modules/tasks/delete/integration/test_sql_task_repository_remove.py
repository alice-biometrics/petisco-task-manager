import pytest

from meiga.assertions import assert_success, assert_failure

from taskmanager.src.modules.tasks.domain.errors import TaskNotFoundError


@pytest.mark.integration
def test_should_remove_task_successfully(
    taskmanager_sql_database, given_a_sql_task_repository_with_a_task, given_any_task_id
):
    repository = given_a_sql_task_repository_with_a_task

    result = repository.remove(given_any_task_id)

    assert_success(result)


@pytest.mark.integration
def test_should_fail_when_remove_task_when_task_is_not_found(
    taskmanager_sql_database, given_empty_sql_task_repository, given_any_task_id
):
    repository = given_empty_sql_task_repository

    result = repository.remove(given_any_task_id)

    assert_failure(result, value_is_instance_of=TaskNotFoundError)
