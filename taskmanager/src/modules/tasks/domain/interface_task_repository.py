from petisco import IRepository


class ITaskRepository(IRepository):
    def save(self, task_id: TaskId, task: Task) -> Result[bool, Error]:
        return NotImplementedMethodError

    def retrieve(self, task_id: TaskId) -> Result[Task, Error]:
        return NotImplementedMethodError
