from typing import Dict

from petisco import controller_handler, Petisco

from taskmanager.src.modules.tasks.application.create.create_task import CreateTask
from taskmanager.src.modules.tasks.application.create.post_task_error_handler import (
    post_task_error_handler,
)
from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.task_id import TaskId
from taskmanager.src.modules.tasks.domain.title import Title


@controller_handler(
    success_handler=lambda result: (
        {"message": "Created Task", "task_id": str(result.value)},
        200,
    ),
    error_handler=post_task_error_handler,
)
def post_task(body: Dict):

    task_id = TaskId.generate()
    title = Title(body.get("title")).guard()
    description = Description(body.get("description")).guard()

    use_case = CreateTask(
        task_repository=Petisco.repositories().task,
        event_manager=Petisco.event_manager(),
    )

    return use_case.execute(task_id, title, description)
