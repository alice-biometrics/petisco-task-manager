from meiga import Result
from petisco import HttpError, EmptyValueObjectError, ExceedLengthLimitValueObjectError


def post_task_error_handler(result: Result) -> HttpError:
    domain_error = result.value
    http_error = HttpError()
    if isinstance(domain_error, EmptyValueObjectError):
        http_error.message = f"Missing Input {domain_error.message}"
        http_error.code = 405
        http_error.type_error = "MissingInputError"
    if isinstance(domain_error, ExceedLengthLimitValueObjectError):
        http_error.message = "Exceed Length Limit"
        http_error.code = 405
        http_error.type_error = "ExceedLengthLimitInputError"
    return http_error
