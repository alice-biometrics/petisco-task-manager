from petisco import controller_handler, Petisco

from taskmanager.src.modules.events.application.retrieve.events_retriever import (
    EventsRetriever,
)
from taskmanager.src.modules.events.application.retrieve.get_events_error_handle import (
    get_events_error_handler,
)


@controller_handler(
    logger=Petisco.get_instance().logger,
    success_handler=lambda result: ({"events": result.value}, 200),
    error_handler=get_events_error_handler,
)
def get_events():
    use_case = EventsRetriever(
        repository=Petisco.get_repository("event"),
        publisher=Petisco.get_event_publisher(),
    )
    return use_case.execute()
