import pytest

from meiga.assertions import assert_success, assert_failure

from taskmanager.src.modules.tasks.domain.errors import TaskAlreadyExistError


@pytest.mark.integration
def test_should_save_task_successfully(
    petisco_sql_database,
    given_empty_sql_task_repository,
    given_any_task_id,
    given_any_task,
):
    repository = given_empty_sql_task_repository

    result = repository.save(given_any_task_id, given_any_task)

    assert_success(result)


@pytest.mark.integration
def test_should_fail_when_save_task_when_already_exist_the_task(
    petisco_sql_database,
    given_a_sql_task_repository_with_a_task,
    given_any_task_id,
    given_any_task,
):
    repository = given_a_sql_task_repository_with_a_task

    result = repository.save(given_any_task_id, given_any_task)

    assert_failure(result, value_is_instance_of=TaskAlreadyExistError)
