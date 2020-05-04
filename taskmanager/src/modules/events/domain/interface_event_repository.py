from meiga import Result, Error, NotImplementedMethodError
from petisco import IRepository, Event, EventId, Events


class IEventRepository(IRepository):
    def save(self, event_id: EventId, event: Event) -> Result[bool, Error]:
        return NotImplementedMethodError

    def retrieve(self, event_id: EventId) -> Result[Event, Error]:
        return NotImplementedMethodError

    def retrieve_all(self) -> Result[Events, Error]:
        return NotImplementedMethodError

    def remove(self, event_id: EventId) -> Result[bool, Error]:
        return NotImplementedMethodError
