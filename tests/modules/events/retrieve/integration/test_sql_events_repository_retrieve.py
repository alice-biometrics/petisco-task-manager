import pytest

from meiga.assertions import assert_success


@pytest.mark.integration
def test_should_retrieve_task_successfully(
    petisco_sql_database, given_a_sql_event_repository_with_some_events
):
    repository = given_a_sql_event_repository_with_some_events

    result = repository.retrieve_all()

    assert_success(result)
    assert len(result.value) == 3


@pytest.mark.integration
def test_should_fail_when_retrieve_task_when_task_is_not_found(
    petisco_sql_database, given_empty_sql_event_repository
):
    repository = given_empty_sql_event_repository

    result = repository.retrieve_all()

    assert_success(result, value_is_equal_to=[])
