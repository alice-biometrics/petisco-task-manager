import os

import pytest

from datetime import datetime

from petisco import Petisco, Events, Persistence

from taskmanager.src.modules.events.infrastructure.persistence.sql_event_repository import (
    SqlEventRepository,
)
from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.events import (
    TaskCreated,
    TaskRemoved,
    TaskRetrieved,
)
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId
from taskmanager.src.modules.tasks.domain.title import Title
from taskmanager.src.modules.tasks.infrastructure.persistence.sql_task_repository import (
    SqlTaskRepository,
)


@pytest.fixture
def petisco_yml_path_flask_app():
    return f"{os.path.dirname(os.path.abspath(__file__))}/../../taskmanager"


@pytest.fixture
def taskmanager_sql_database():
    persistence = Persistence()
    persistence.create()

    yield

    persistence.delete()


@pytest.fixture
def petisco_client_flask_app(taskmanager_sql_database):
    app = Petisco.get_instance().get_app()
    with app.app.test_client() as c:
        yield c
    Petisco.get_instance().stop()


@pytest.fixture
def given_any_task_id() -> TaskId:
    return TaskId("37d0e87b-582e-4ca9-9668-218ef4fed709")


@pytest.fixture
def given_any_title() -> Title:
    return Title("Release new petisco version")


@pytest.fixture
def given_any_description() -> Description:
    return Description(
        "New release should contain the following improvements: \n* Performance improvement\n* AggregateRoot utilities"
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
def given_empty_sql_task_repository():
    return SqlTaskRepository.build()


@pytest.fixture
def given_a_sql_task_repository_with_a_task(
    given_empty_sql_task_repository, given_any_task_id, given_any_task
):
    repository = given_empty_sql_task_repository
    repository.save(given_any_task_id, given_any_task)
    return repository


@pytest.fixture
def given_empty_sql_event_repository():
    return SqlEventRepository.build()


@pytest.fixture
def given_some_events(given_any_task_id):
    events: Events = [
        TaskCreated(given_any_task_id),
        TaskRemoved(given_any_task_id),
        TaskRetrieved(given_any_task_id),
    ]
    return events


@pytest.fixture
def given_a_sql_event_repository_with_some_events(
    given_empty_sql_event_repository, given_some_events
):
    repository = given_empty_sql_event_repository
    for event in given_some_events:
        repository.save(event.event_id, event)
    return repository
