from typing import Dict, Callable
from meiga import Result, Error, isSuccess, Failure, Success

from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.errors import (
    TaskAlreadyExistError,
    TaskNotFoundError,
)
from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId
from taskmanager.src.modules.tasks.domain.title import Title


class SqlTaskRepository(ITaskRepository):
    def __init__(self, session_scope: Callable, task_model):
        self.session_scope = session_scope
        self.TaskModel = task_model

    def info(self) -> Dict:
        return {"name": self.__class__.__name__}

    def save(self, task_id: TaskId, task: Task) -> Result[bool, Error]:
        with self.session_scope("petisco") as session:
            task_model = (
                session.query(self.TaskModel)
                .filter(self.TaskModel.task_id == task_id.value)
                .first()
            )
            if task_model:
                return Failure(TaskAlreadyExistError(task_id))

            task_model = self.TaskModel(
                task_id=task_id.value,
                title=task.title.value,
                description=task.description.value,
                created_at=task.created_at,
            )

            session.add(task_model)
            return isSuccess

    def retrieve(self, task_id: TaskId) -> Result[Task, Error]:
        with self.session_scope("petisco") as session:
            task_model = (
                session.query(self.TaskModel)
                .filter(self.TaskModel.task_id == task_id.value)
                .first()
            )
            if not task_model:
                return Failure(TaskNotFoundError(task_id))

            task = Task(
                task_id=TaskId(task_model.task_id),
                title=Title(task_model.title),
                description=Description(task_model.description),
                created_at=task_model.created_at,
            )

            return Success(task)

    def remove(self, task_id: TaskId) -> Result[Task, Error]:
        with self.session_scope("petisco") as session:
            task_model = (
                session.query(self.TaskModel)
                .filter(self.TaskModel.task_id == task_id.value)
                .first()
            )
            if not task_model:
                return Failure(TaskNotFoundError(task_id))

            session.delete(task_model)

            return isSuccess
