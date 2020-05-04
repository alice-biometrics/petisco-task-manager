from meiga import Result
from petisco import controller_handler, Petisco

from taskmanager.src.modules.events.application.retrieve.events_retriever import (
    EventsRetriever,
)


def success_handler(result: Result):
    events = [event.to_dict() for event in result.value]
    return {"events": events}, 200


@controller_handler(
    logger=Petisco.get_instance().logger, success_handler=success_handler
)
def get_events():
    use_case = EventsRetriever(
        repository=Petisco.get_repository("event"),
        publisher=Petisco.get_event_publisher(),
    )
    return use_case.execute()
