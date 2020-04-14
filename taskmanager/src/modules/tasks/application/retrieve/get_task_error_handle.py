from meiga import Result
from petisco.controller.errors.http_error import HttpError

from taskmanager.src.modules.tasks.domain.errors import TaskNotFoundError


class TaskNotFoundHttpError(HttpError):
    def __init__(self, message: str = "Task not found", code: int = 404):
        self.message = message
        self.code = code
        super(TaskNotFoundHttpError, self).__init__(message, code)


def get_task_error_handler(result: Result) -> HttpError:
    domain_error = result.value
    http_error = HttpError()
    if isinstance(domain_error, TaskNotFoundError):
        http_error = TaskNotFoundHttpError()
    return http_error
