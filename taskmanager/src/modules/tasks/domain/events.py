from petisco import Event

from taskmanager.src.modules.tasks.domain.task_id import TaskId


class TaskCreated(Event):
    task_id: str

    def __init__(self, task_id: TaskId):
        self.task_id = str(task_id)
        self.event_version = "1"
        super().__init__()


class TaskRemoved(Event):
    task_id: str

    def __init__(self, task_id: TaskId):
        self.task_id = str(task_id)
        self.event_version = "1"
        super().__init__()


class TaskRetrieved(Event):
    task_id: str

    def __init__(self, task_id: TaskId):
        self.task_id = str(task_id)
        self.event_version = "1"
        super().__init__()
