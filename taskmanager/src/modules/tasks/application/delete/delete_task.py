from petisco import controller_handler

from taskmanager.src.modules.tasks.application.delete.delete_task_error_handle import (
    delete_task_error_handler,
)
from taskmanager.src.modules.tasks.application.delete.task_remover import TaskRemover
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@controller_handler(
    success_handler=lambda result: ({"message": "Task deleted"}, 200),
    error_handler=delete_task_error_handler,
)
def delete_task(task_id: str):
    task_id = TaskId(task_id)
    return TaskRemover.build().execute(task_id)
