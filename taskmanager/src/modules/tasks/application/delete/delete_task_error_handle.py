from meiga import Result
from petisco.controller.errors.http_error import HttpError

from taskmanager.src.modules.tasks.domain.errors import TaskNotFoundError


def delete_task_error_handler(result: Result) -> HttpError:
    domain_error = result.value
    http_error = HttpError()
    if isinstance(domain_error, TaskNotFoundError):
        http_error.message = "Task not found"
        http_error.code = 404
        http_error.type_error = "TaskNotFoundError"
    return http_error
