import pytest

from datetime import datetime

from petisco import Petisco

from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId
from taskmanager.src.modules.tasks.domain.title import Title
from taskmanager.src.modules.tasks.infrastructure.persistence.sql_task_repository import (
    SqlTaskRepository,
)


@pytest.fixture
def given_any_task_id() -> TaskId:
    return TaskId("5t5qXjRuYFasoS28")


@pytest.fixture
def given_any_title() -> Title:
    return Title("Release new petisco version")


@pytest.fixture
def given_any_description() -> Description:
    return Description(
        "New release should contain the following improvements: \n"
        " * Performance improvement\n"
        " * AggregateRoot utilities"
    )


@pytest.fixture
def given_any_task(given_any_task_id, given_any_title, given_any_description) -> Task:
    return Task(
        given_any_task_id,
        given_any_title,
        given_any_description,
        datetime.strptime("1/1/2019 1:30 PM", "%m/%d/%Y %I:%M %p"),
    )


@pytest.fixture
def given_empty_sql_task_repository(given_any_task_id, given_any_task):
    repository = SqlTaskRepository(
        session_scope=Petisco.persistence_session_scope(),
        task_model=Petisco.persistence_models().get("task"),
    )
    return repository


@pytest.fixture
def given_a_sql_task_repository_with_a_task(given_any_task_id, given_any_task):
    repository = SqlTaskRepository(
        session_scope=Petisco.persistence_session_scope(),
        task_model=Petisco.persistence_models().get("task"),
    )
    repository.save(given_any_task_id, given_any_task)
    return repository
