from petisco import use_case_handler, UseCase, Event

from meiga import Result, Error, isSuccess

from taskmanager.src.modules.events.domain.interface_event_repository import (
    IEventRepository,
)


@use_case_handler()
class EventStorer(UseCase):
    def __init__(self, event_repository: IEventRepository):
        self.event_repository = event_repository

    def execute(self, event: Event) -> Result[bool, Error]:

        self.self.event_repository.save(event.event_id, event).unwrap_or_return()

        return isSuccess
