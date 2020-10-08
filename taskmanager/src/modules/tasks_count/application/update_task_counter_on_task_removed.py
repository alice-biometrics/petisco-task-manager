from meiga import BoolResult
from petisco import event_handler, Event

from taskmanager.src.modules.tasks_count.application.tasks_count_decreaser import (
    TasksCountDecreaser,
)


@event_handler()
def update_task_counter_on_task_removed(event: Event) -> BoolResult:
    return TasksCountDecreaser.build().execute()
