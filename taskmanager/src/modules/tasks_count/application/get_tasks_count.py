from meiga import Result

from petisco import controller_handler

from taskmanager.src.modules.tasks_count.application.tasks_count_retriever import (
    TasksCountRetriever,
)


def success_handler(result: Result):
    return {"tasks_count": result.value}, 200


@controller_handler(success_handler=success_handler)
def get_tasks_count():
    return TasksCountRetriever.build().execute()
