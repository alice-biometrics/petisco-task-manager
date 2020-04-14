from petisco import use_case_handler, UseCase, IEventManager

from meiga import Result, Error, isSuccess

from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.title import Title

isSuccess


from taskmanager.src.modules.tasks.domain.interface_task_repository import ITaskRepository
from taskmanager.src.modules.tasks.domain.task import Task
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@use_case_handler(
    logging_parameters_whitelist=["task_id"]
)
class RetrieveTask(UseCase):
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: TaskId) -> Result[Task, Error]:
        return self.task_repository.retrieve(task_id)
