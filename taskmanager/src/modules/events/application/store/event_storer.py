from petisco import use_case_handler, UseCase, Event, Petisco

from meiga import Result, Error, isSuccess

from taskmanager.src.modules.events.domain.interface_event_repository import (
    IEventRepository,
)


@use_case_handler()
class EventStorer(UseCase):
    @staticmethod
    def build():
        return EventStorer(repository=Petisco.get_repository("event"))

    def __init__(self, repository: IEventRepository):
        self.repository = repository

    def execute(self, event: Event) -> Result[bool, Error]:

        self.repository.save(event.event_id, event).unwrap_or_return()

        return isSuccess
