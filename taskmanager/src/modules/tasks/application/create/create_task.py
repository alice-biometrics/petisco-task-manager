from petisco import use_case_handler, UseCase, Petisco, Repositories

from meiga import Result, Error, Success
from petisco.event.bus.domain.interface_event_bus import IEventBus

from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.title import Title

from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@use_case_handler(logging_parameters_whitelist=["task_id", "title", "description"])
class CreateTask(UseCase):
    @staticmethod
    def build():
        return CreateTask(
            repository=Repositories.get("task"), bus=Petisco.get_event_bus()
        )

    def __init__(self, repository: ITaskRepository, bus: IEventBus):
        self.repository = repository
        self.bus = bus

    def execute(
        self, task_id: TaskId, title: Title, description: Description
    ) -> Result[TaskId, Error]:
        task = Task.create(task_id, title, description)
        self.repository.save(task_id, task).unwrap_or_return()
        self.bus.publish_events(task.pull_domain_events())
        return Success(task_id)
