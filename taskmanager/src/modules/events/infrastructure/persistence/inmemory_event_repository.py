from typing import Dict
from meiga import Result, Error, isSuccess, Failure, Success
from petisco import EventId, Event, Events

from taskmanager.src.modules.events.domain.errors import (
    EventAlreadyExistError,
    EventNotFoundError,
)
from taskmanager.src.modules.events.domain.interface_event_repository import (
    IEventRepository,
)


class InMemoryEventRepository(IEventRepository):
    def __init__(self):
        self.events = {}

    def info(self) -> Dict:
        return {"name": self.__class__.__name__}

    def save(self, event_id: EventId, event: Event) -> Result[bool, Error]:
        if str(event_id) in self.events:
            return Failure(EventAlreadyExistError(event_id))
        self.events[str(event_id)] = event
        return isSuccess

    def retrieve(self, event_id: EventId) -> Result[Event, Error]:
        if str(event_id) not in self.events:
            return Failure(EventNotFoundError(event_id))
        return Success(self.events[str(event_id)])

    def retrieve_all(self) -> Result[Events, Error]:
        return Success(list(self.events.values()))

    def remove(self, event_id: EventId) -> Result[bool, Error]:
        if str(event_id) not in self.events:
            return Failure(EventNotFoundError(event_id))
        self.events.pop(str(event_id))
        return isSuccess
