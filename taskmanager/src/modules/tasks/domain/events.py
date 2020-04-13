from petisco import Event, TaskId


EVENT_TASK_CREATED_VERSION = "1.0.0"


class TaskCreated(Event):
    task_id: str

    def __init__(self, task_id: TaskId, version: str = EVENT_TASK_CREATED_VERSION):
        self.task_id = str(task_id)
        self.event_version = version
        super().__init__()
