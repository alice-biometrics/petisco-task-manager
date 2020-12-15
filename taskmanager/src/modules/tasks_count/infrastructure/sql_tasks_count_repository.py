from typing import Any, Callable

from meiga import Result, Error, isSuccess, Success

from petisco import Persistence

from taskmanager.src.modules.tasks_count.domain.interface_tasks_count_repository import (
    ITasksCountRepository,
)


class SqlTasksCountCountRepository(ITasksCountRepository):
    @staticmethod
    def build():
        return SqlTasksCountCountRepository(
            session_scope=Persistence.get_session_scope("taskmanager"),
            tasks_count_model=Persistence.get_model("taskmanager", "tasks_count"),
        )

    def __init__(self, session_scope: Callable, tasks_count_model: Any):
        self.session_scope = session_scope
        self.TasksCountModel = tasks_count_model

    def increase(self) -> Result[bool, Error]:
        with self.session_scope() as session:
            users_count_model = session.query(self.TasksCountModel).first()
            if not users_count_model:
                users_count_model = self.TasksCountModel(count=1)
                session.add(users_count_model)
                return isSuccess

            users_count_model.count += 1

            return isSuccess

    def decrease(self) -> Result[bool, Error]:
        with self.session_scope() as session:
            users_count_model = session.query(self.TasksCountModel).first()
            if not users_count_model:
                users_count_model = self.TasksCountModel(count=0)
                session.add(users_count_model)
                return isSuccess

            users_count_model.count -= 1
            return isSuccess

    def count(self) -> Result[int, Error]:
        with self.session_scope() as session:
            users_count_model = session.query(self.TasksCountModel).first()
            if not users_count_model:
                return Success(0)

            return Success(users_count_model.count)
