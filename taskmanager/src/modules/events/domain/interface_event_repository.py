from meiga import Result, Error, NotImplementedMethodError
from petisco import IRepository, Event, EventId

from taskmanager.src.modules.tasks.domain.task import Task


class IEventRepository(IRepository):
    def save(self, event_id: EventId, event: Event) -> Result[bool, Error]:
        return NotImplementedMethodError

    def retrieve(self, event_id: EventId) -> Result[Task, Error]:
        return NotImplementedMethodError

    def remove(self, event_id: EventId) -> Result[bool, Error]:
        return NotImplementedMethodError
