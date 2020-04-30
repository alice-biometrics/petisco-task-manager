from petisco import use_case_handler, UseCase, IEventPublisher

from meiga import Result, Error, Success

from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.title import Title

from taskmanager.src.modules.tasks.domain.interface_task_repository import (
    ITaskRepository,
)
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@use_case_handler(logging_parameters_whitelist=["task_id", "title", "description"])
class CreateTask(UseCase):
    def __init__(self, repository: ITaskRepository, publisher: IEventPublisher):
        self.repository = repository
        self.publisher = publisher

    def execute(
        self, task_id: TaskId, title: Title, description: Description
    ) -> Result[TaskId, Error]:
        task = Task.create(task_id, title, description)
        self.repository.save(task_id, task).unwrap_or_return()
        self.publisher.publish_list(task.pull_domain_events())
        return Success(task_id)
