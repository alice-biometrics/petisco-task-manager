import os
from typing import Dict

from petisco import IRepository

from taskmanager.src.modules.tasks.domain.interface_task_repository import ITaskRepository
from taskmanager.src.modules.tasks.infrastructure.inmemory_task_repository import InMemoryTaskRepository


def repositories_provider() -> Dict[str, IRepository]:
    return {"task": get_config_task_repository()}


def get_config_task_repository() -> ITaskRepository:
    return InMemoryTaskRepository()
