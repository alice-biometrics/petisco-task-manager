from meiga import Error
from petisco import EventId


class EventAlreadyExistError(Error):
    def __init__(self, event_id: EventId):
        self.message = f"[event_id: {event_id:s}]"


class EventNotFoundError(Error):
    def __init__(self, event_id: EventId):
        self.message = f"[event_id: {event_id:s}]"
