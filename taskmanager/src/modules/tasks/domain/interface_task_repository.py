from meiga import Result, Error, NotImplementedMethodError
from petisco import IRepository

from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId


class ITaskRepository(IRepository):
    def save(self, task_id: TaskId, task: Task) -> Result[bool, Error]:
        return NotImplementedMethodError

    def retrieve(self, task_id: TaskId) -> Result[Task, Error]:
        return NotImplementedMethodError
