from petisco import use_case_handler, UseCase, IEventPublisher, Petisco

from meiga import Result, Error, isSuccess

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
            repository=Petisco.get_repository("task"),
            publisher=Petisco.get_event_publisher(),
        )

    def __init__(self, repository: ITaskRepository, publisher: IEventPublisher):
        self.repository = repository
        self.publisher = publisher

    def execute(self, task_id: TaskId) -> Result[bool, Error]:
        self.repository.remove(task_id).unwrap_or_return()
        self.publisher.publish(TaskRemoved(task_id))
        return isSuccess
