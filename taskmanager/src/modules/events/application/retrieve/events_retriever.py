from petisco import use_case_handler, UseCase, IEventPublisher, Events

from meiga import Result, Error, Success

from taskmanager.src.modules.events.domain.events import EventsRetrieved
from taskmanager.src.modules.events.domain.interface_event_repository import (
    IEventRepository,
)


@use_case_handler()
class EventsRetriever(UseCase):
    def __init__(self, repository: IEventRepository, publisher: IEventPublisher):
        self.repository = repository
        self.publisher = publisher

    def execute(self) -> Result[Events, Error]:
        events = self.repository.retrieve_all().unwrap_or_return()
        self.publisher.publish(EventsRetrieved())
        return Success(events)
