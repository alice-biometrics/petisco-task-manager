from typing import Any, Callable

from meiga import Result, Error, isSuccess, Success

from petisco import Petisco

from taskmanager.src.modules.tasks_count.domain.interface_tasks_count_repository import (
    ITasksCountRepository,
)


class SqlTasksCountCountRepository(ITasksCountRepository):
    @staticmethod
    def build():
        return SqlTasksCountCountRepository(
            session_scope=Petisco.persistence_session_scope(),
            tasks_count_model=Petisco.get_persistence_model("petisco", "tasks_count"),
        )

    def __init__(self, session_scope: Callable, tasks_count_model: Any):
        self.session_scope = session_scope
        self.TasksCountModel = tasks_count_model

    def increase(self) -> Result[bool, Error]:
        with self.session_scope("petisco") as session:
            users_count_model = session.query(self.TasksCountModel).first()
            if not users_count_model:
                users_count_model = self.TasksCountModel(count=1)
                session.add(users_count_model)
                return isSuccess

            users_count_model.count += 1

            return isSuccess

    def decrease(self) -> Result[bool, Error]:
        with self.session_scope("petisco") as session:
            users_count_model = session.query(self.TasksCountModel).first()
            if not users_count_model:
                users_count_model = self.TasksCountModel(count=0)
                session.add(users_count_model)
                return isSuccess

            users_count_model.count -= 1
            return isSuccess

    def count(self) -> Result[int, Error]:
        with self.session_scope("petisco") as session:
            users_count_model = session.query(self.TasksCountModel).first()
            if not users_count_model:
                return Success(0)

            return Success(users_count_model.count)
