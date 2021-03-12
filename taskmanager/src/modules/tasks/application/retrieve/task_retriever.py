from petisco import use_case_handler, UseCase, Petisco, IEventBus, Repositories

from meiga import Result, Error, Success

from taskmanager.src.modules.tasks.domain.events import TaskRetrieved
from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@use_case_handler(logging_parameters_whitelist=["task_id"])
class TaskRetriever(UseCase):
    @staticmethod
    def build():
        return TaskRetriever(
            repository=Repositories.get("task"), bus=Petisco.get_event_bus()
        )

    def __init__(self, repository: ITaskRepository, bus: IEventBus):
        self.repository = repository
        self.bus = bus

    def execute(self, task_id: TaskId) -> Result[Task, Error]:
        task = self.repository.retrieve(task_id).unwrap_or_return()
        self.bus.publish(TaskRetrieved(task_id))
        return Success(task)
