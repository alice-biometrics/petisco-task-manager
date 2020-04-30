from typing import Dict
from meiga import Result, Error, isSuccess, Failure, Success
from petisco import EventId, Event

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
        if event_id in self.events:
            return Failure(EventAlreadyExistError(event_id))
        self.events[event_id] = event
        return isSuccess

    def retrieve(self, event_id: EventId) -> Result[Event, Error]:
        if event_id not in self.events:
            return Failure(EventNotFoundError(event_id))
        return Success(self.events[event_id])

    def remove(self, event_id: EventId) -> Result[bool, Error]:
        if event_id not in self.events:
            return Failure(EventNotFoundError(event_id))
        self.events.pop(event_id)
        return isSuccess
