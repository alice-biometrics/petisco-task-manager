from petisco import use_case_handler, UseCase, IEventManager

from meiga import Result, Error, Success

from taskmanager import TASK_MANAGER_EVENT_TOPIC
from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.title import Title

from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@use_case_handler(logging_parameters_whitelist=["task_id", "title", "description"])
class CreateTask(UseCase):
    def __init__(self, task_repository: ITaskRepository, event_manager: IEventManager):
        self.task_repository = task_repository
        self.event_manager = event_manager

    def execute(
        self, task_id: TaskId, title: Title, description: Description
    ) -> Result[TaskId, Error]:

        task = Task.create(task_id, title, description)
        self.task_repository.save(task_id, task).unwrap_or_return()
        self.event_manager.publish_list(
            TASK_MANAGER_EVENT_TOPIC, task.pull_domain_events()
        )
        return Success(task_id)
