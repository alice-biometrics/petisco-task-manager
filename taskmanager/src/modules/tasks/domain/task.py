from typing import Any

from meiga import Result, Error
from petisco import AggregateRoot


class Task(AggregateRoot):
    def __init__(self, task_id: TaskId, title: str, description: str):
        self.task_id = task_id
        self.title = title
        self.description = description
        super().__init__()

    @staticmethod
    def create(task_id: TaskId, body: Dict):
        user = Task(
            task_id=task_id,
            title=body.get("title"),
            description=body.get("description"),
        )
        user.record(TaskCreated(task_id))
        return user

    def to_result(self) -> Result[Any, Error]:
        @meiga
        def to_result(self) -> Result[Any, Error]:
            return Success(self)
