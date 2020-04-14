from typing import Dict

from meiga import Result
from petisco import controller_handler, HttpError, Petisco

from taskmanager.src.modules.tasks.application.retrieve.retrieve_task import (
    RetrieveTask,
)
from taskmanager.src.modules.tasks.domain.task_id import TaskId


def error_handler(result: Result):
    # domain_error = result.value
    return HttpError()


@controller_handler(
    success_handler=lambda result: ({"task": result.value.to_dict()}, 200),
    error_handler=error_handler,
)
def get_task(body: Dict):

    task_id = TaskId(body.get("task_id")).guard()

    use_case = RetrieveTask(task_repository=Petisco.repositories().task)

    return use_case.execute(task_id)
