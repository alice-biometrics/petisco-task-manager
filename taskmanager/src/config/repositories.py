import os
from typing import Dict

from petisco import IRepository, Petisco

from taskmanager.src.modules.events.domain.interface_event_repository import (
    IEventRepository,
)
from taskmanager.src.modules.events.infrastructure.persistence.inmemory_event_repository import (
    InMemoryEventRepository,
)
from taskmanager.src.modules.events.infrastructure.persistence.sql_event_repository import (
    SqlEventRepository,
)
from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)
from taskmanager.src.modules.tasks.infrastructure.persistence.inmemory_task_repository import (
    InMemoryTaskRepository,
)
from taskmanager.src.modules.tasks.infrastructure.persistence.sql_task_repository import (
    SqlTaskRepository,
)


def repositories_provider() -> Dict[str, IRepository]:
    return {
        "task": get_config_task_repository(),
        "event": get_config_event_repository(),
    }


def get_config_task_repository() -> ITaskRepository:
    task_repository_type = os.environ.get("TASK_REPOSITORY_TYPE")
    task_repository = InMemoryTaskRepository()
    if task_repository_type == "sqlite" or task_repository_type == "mysql":
        task_repository = SqlTaskRepository(
            session_scope=Petisco.persistence_session_scope(),
            task_model=Petisco.get_persistence_model("task"),
        )
    return task_repository


def get_config_event_repository() -> IEventRepository:
    event_repository_type = os.environ.get("EVENT_REPOSITORY_TYPE")
    event_repository = InMemoryEventRepository()
    if event_repository_type == "sqlite" or event_repository_type == "mysql":
        event_repository = SqlEventRepository(
            session_scope=Petisco.persistence_session_scope(),
            event_model=Petisco.get_persistence_model("event"),
        )
    return event_repository
