from meiga import Result, Error

from petisco import UseCase, use_case_handler, Repositories

from taskmanager.src.modules.tasks_count.domain.interface_tasks_count_repository import (
    ITasksCountRepository,
)


@use_case_handler()
class TasksCountIncreaser(UseCase):
    @staticmethod
    def build():
        return TasksCountIncreaser(repository=Repositories.get("tasks_count"))

    def __init__(self, repository: ITasksCountRepository):
        self.repository = repository

    def execute(self) -> Result[bool, Error]:
        return self.repository.increase()
