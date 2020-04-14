import pytest

from datetime import datetime

from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId
from taskmanager.src.modules.tasks.domain.title import Title


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
