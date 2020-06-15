from meiga import Result
from petisco.controller.errors.http_error import HttpError
from petisco.domain.value_objects.uuid import InvalidUuidError

from taskmanager.src.modules.tasks.domain.errors import TaskNotFoundError


def get_task_error_handler(result: Result) -> HttpError:
    domain_error = result.value
    http_error = HttpError()
    if isinstance(domain_error, TaskNotFoundError):
        http_error.message = "Task not found"
        http_error.code = 404
        http_error.type_error = "TaskNotFoundError"
    elif isinstance(domain_error, InvalidUuidError):
        http_error.message = "Invalid TaskId. TaskId must be a valid 36-char UUID"
        http_error.code = 400
        http_error.type_error = "InvalidTaskIdError"
    return http_error
