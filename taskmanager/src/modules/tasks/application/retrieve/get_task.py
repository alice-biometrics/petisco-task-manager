from petisco import controller_handler, Petisco

from taskmanager.src.modules.tasks.application.retrieve.get_task_error_handle import (
    get_task_error_handler,
)
from taskmanager.src.modules.tasks.application.retrieve.retrieve_task import (
    RetrieveTask,
)
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@controller_handler(
    success_handler=lambda result: ({"task": result.value.to_dict()}, 200),
    error_handler=get_task_error_handler,
)
def get_task(task_id: str):
    task_id = TaskId(task_id).guard()

    use_case = RetrieveTask(task_repository=Petisco.repositories().task)

    return use_case.execute(task_id)
