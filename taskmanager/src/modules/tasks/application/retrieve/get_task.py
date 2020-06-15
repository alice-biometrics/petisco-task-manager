from petisco import controller_handler

from taskmanager.src.modules.tasks.application.retrieve.get_task_error_handle import (
    get_task_error_handler,
)
from taskmanager.src.modules.tasks.application.retrieve.task_retriever import (
    TaskRetriever,
)
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@controller_handler(
    success_handler=lambda result: ({"task": result.value.to_dict()}, 200),
    error_handler=get_task_error_handler,
)
def get_task(task_id: str):

    task_id = TaskId(task_id)

    return TaskRetriever.build().execute(task_id)
