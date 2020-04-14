from meiga import Result
from petisco import HttpError, EmptyValueObjectError


class MissingInputHttpError(HttpError):
    def __init__(self, message: str = "Missing Input", code: int = 405):
        self.message = message
        self.code = code
        super(MissingInputHttpError, self).__init__(message, code)


def post_task_error_handler(result: Result) -> HttpError:
    domain_error = result.value
    http_error = HttpError()
    if isinstance(domain_error, EmptyValueObjectError):
        http_error = MissingInputHttpError(f"Missing Input {domain_error.message}")
    return http_error
