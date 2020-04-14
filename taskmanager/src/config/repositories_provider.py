import os
from typing import Dict

from petisco import IRepository, Petisco

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
    return {"task": get_config_task_repository()}


def get_config_task_repository() -> ITaskRepository:

    task_repository_type = os.environ.get("TASK_REPOSITORY_TYPE")
    if not task_repository_type or task_repository_type == "inmemory":
        task_repository = InMemoryTaskRepository()
    elif task_repository_type == "sqlite" or task_repository_type == "mysql":
        task_repository = SqlTaskRepository(
            session_scope=Petisco.persistence_session_scope(),
            task_model=Petisco.persistence_models().get("task"),
        )

    return task_repository
