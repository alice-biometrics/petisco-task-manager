from typing import Dict

from meiga import Result
from petisco import controller_handler, InfoId, HttpError, Petisco

from taskmanager.src.modules.tasks.application.create.create_task import CreateTask
from taskmanager.src.modules.tasks.domain.description import Description
from taskmanager.src.modules.tasks.domain.task_id import TaskId
from taskmanager.src.modules.tasks.domain.title import Title


def error_handler(result: Result):
    domain_error = result.value
    return HttpError()


@controller_handler(
    success_handler=lambda result: ({"message": "Created Task"}, 200),
    error_handler=error_handler,
)
def post_task(body: Dict):

    task_id = TaskId.generate()
    title = Title(body.get("title")).guard()
    description = Description(body.get("description")).guard()

    use_case = CreateTask(task_repository=Petisco.repositories().task,
                          event_manager=Petisco.event_manager())

    return use_case.execute(task_id, title, description)
