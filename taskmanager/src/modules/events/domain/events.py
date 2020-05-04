from petisco import Event


class EventsRetrieved(Event):
    def __init__(self):
        self.event_version = "1"
        super().__init__()
