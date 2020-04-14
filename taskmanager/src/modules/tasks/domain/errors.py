from meiga import Error

from taskmanager.src.modules.tasks.domain.task_id import TaskId


class TaskAlreadyExistError(Error):
    def __init__(self, task_id: TaskId):
        self.message = f"[task_id: {task_id:s}]"


class TaskNotFoundError(Error):
    def __init__(self, task_id: TaskId):
        self.message = f"[task_id: {task_id:s}]"
