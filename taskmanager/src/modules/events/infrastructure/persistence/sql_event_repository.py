from typing import Dict, Callable
from meiga import Result, Error, isSuccess, Failure, Success
from petisco import EventId, Event, Events

from taskmanager.src.modules.events.domain.errors import (
    EventAlreadyExistError,
    EventNotFoundError,
)
from taskmanager.src.modules.events.domain.interface_event_repository import (
    IEventRepository,
)


class SqlEventRepository(IEventRepository):
    def __init__(self, session_scope: Callable, event_model):
        self.session_scope = session_scope
        self.EventModel = event_model

    def info(self) -> Dict:
        return {"name": self.__class__.__name__}

    def save(self, event_id: EventId, event: Event) -> Result[bool, Error]:
        with self.session_scope("petisco") as session:
            event_model = (
                session.query(self.EventModel)
                .filter(self.EventModel.event_id == event_id.value)
                .first()
            )
            if event_model:
                return Failure(EventAlreadyExistError(event_id))

            event_model = self.EventModel(
                event_id=event_id.value, type=event.event_name, data=event.to_json()
            )
            session.add(event_model)
            return isSuccess

    def retrieve(self, event_id: EventId) -> Result[Event, Error]:
        with self.session_scope("petisco") as session:
            event_model = (
                session.query(self.EventModel)
                .filter(self.EventModel.event_id == event_id.value)
                .first()
            )
            if not event_model:
                return Failure(EventNotFoundError(event_id))

            event = Event.from_json(event_model.data)

            return Success(event)

    def retrieve_all(self) -> Result[Events, Error]:
        with self.session_scope("petisco") as session:
            event_models = session.query(self.EventModel).all()
            events: Events = []
            if event_models:
                for event_model in event_models:
                    events.append(Event.from_json(event_model.data))

            return Success(events)
