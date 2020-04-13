from meiga import Result
from petisco import controller_handler, InfoId, HttpError


def error_handler(result: Result):
    domain_error = result.value
    return HttpError()


@controller_handler(
    success_handler=lambda result: ({"message": "Created Task"}, 200),
    error_handler=error_handler,
)
def post_task(info_id: InfoId):
    use_case = CreateTask(task_repository=Petisco.repositories().task)
    return use_case.execute(info_id=info_id)
