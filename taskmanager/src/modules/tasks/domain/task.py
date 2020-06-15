from typing import Dict

from petisco import AggregateRoot
from datetime import datetime

from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.events import TaskCreated
from taskmanager.src.modules.tasks.domain.task_id import TaskId
from taskmanager.src.modules.tasks.domain.title import Title


class Task(AggregateRoot):
    def __init__(
        self,
        task_id: TaskId,
        title: Title,
        description: Description,
        created_at: datetime,
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.created_at = created_at
        super().__init__()

    @staticmethod
    def create(task_id: TaskId, title: Title, description: Description):
        user = Task(task_id, title, description, datetime.utcnow())
        user.record(TaskCreated(task_id))
        return user

    def to_dict(self) -> Dict:
        return {
            "task_id": self.task_id.value,
            "title": self.title.value,
            "description": self.description.value,
            "created_at": self.created_at.isoformat(),
        }
