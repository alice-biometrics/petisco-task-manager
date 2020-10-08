from meiga import BoolResult
from petisco import Petisco, Event, subscriber_handler, event_handler

from taskmanager.src.modules.events.application.store.event_storer import EventStorer


@subscriber_handler(logger=Petisco.get_instance().logger)
def legacy_event_store(event: Event):
    return EventStorer.build().execute(event)


@event_handler()
def event_store(event: Event) -> BoolResult:
    return EventStorer.build().execute(event)
