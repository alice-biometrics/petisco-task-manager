from typing import Dict
from meiga import Result, Error, isSuccess, Failure

from taskmanager.src.modules.tasks.domain.errors import (
    TaskAlreadyExistError,
    TaskNotFoundError,
)
from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = {}

    def info(self) -> Dict:
        return {"name": self.__class__.__name__}

    def save(self, task_id: TaskId, task: Task) -> Result[bool, Error]:
        if task_id in self.tasks:
            return Failure(TaskAlreadyExistError(task_id))
        self.tasks[task_id] = task
        return isSuccess

    def retrieve(self, task_id: TaskId) -> Result[Task, Error]:
        if task_id not in self.tasks:
            return Failure(TaskNotFoundError(task_id))
        return self.tasks[task_id]
