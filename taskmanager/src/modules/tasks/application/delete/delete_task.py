from petisco import controller_handler, Petisco

from taskmanager.src.modules.tasks.application.delete.delete_task_error_handle import (
    delete_task_error_handler,
)
from taskmanager.src.modules.tasks.application.delete.task_remover import TaskRemover
from taskmanager.src.modules.tasks.domain.task_id import TaskId


@controller_handler(
    logger=Petisco.get_instance().logger,
    success_handler=lambda result: ({"message": "Task deleted"}, 200),
    error_handler=delete_task_error_handler,
)
def delete_task(task_id: str):

    task_id = TaskId(task_id).guard()

    use_case = TaskRemover(
        repository=Petisco.repositories().task, publisher=Petisco.get_event_publisher()
    )

    return use_case.execute(task_id)
