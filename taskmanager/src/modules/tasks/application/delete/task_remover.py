from petisco import use_case_handler, UseCase, Petisco

from meiga import Result, Error, isSuccess
from petisco.event.bus.domain.interface_event_bus import IEventBus

from taskmanager.src.modules.tasks.domain.events import TaskRemoved
from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@use_case_handler(logging_parameters_whitelist=["task_id"])
class TaskRemover(UseCase):
    @staticmethod
    def build():
        return TaskRemover(
            repository=Petisco.get_repository("task"), bus=Petisco.get_event_bus()
        )

    def __init__(self, repository: ITaskRepository, bus: IEventBus):
        self.repository = repository
        self.bus = bus

    def execute(self, task_id: TaskId) -> Result[bool, Error]:
        self.repository.remove(task_id).unwrap_or_return()
        self.bus.publish(TaskRemoved(task_id))
        return isSuccess
