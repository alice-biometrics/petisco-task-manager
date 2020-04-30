from petisco import Petisco, Event, subscriber_handler

from taskmanager.src.modules.events.application.store.event_storer import EventStorer


@subscriber_handler(logger=Petisco.get_instance().logger)
def event_store(event: Event):

    use_case = EventStorer(repository=Petisco.get_repository("event"))

    return use_case.execute(event)
