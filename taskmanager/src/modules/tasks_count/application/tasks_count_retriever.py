from meiga import Result, Error

from petisco import UseCase, use_case_handler, Petisco

from taskmanager.src.modules.tasks_count.domain.interface_tasks_count_repository import (
    ITasksCountRepository,
)


@use_case_handler()
class TasksCountRetriever(UseCase):
    @staticmethod
    def build():
        return TasksCountRetriever(repository=Petisco.get_repository("tasks_count"))

    def __init__(self, repository: ITasksCountRepository):
        self.repository = repository

    def execute(self) -> Result[int, Error]:
        return self.repository.count()
