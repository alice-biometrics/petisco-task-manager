from meiga import Error


class TaskAlreadyExistError(Error):
    def __init__(self, task_id: TaskId):
        self.message = f"[task_id: {task_id:s}]"


class TaskNotFoundError(Error):
    def __init__(self, task_id: TaskId):
        self.message = f"[task_id: {task_id:s}]"
