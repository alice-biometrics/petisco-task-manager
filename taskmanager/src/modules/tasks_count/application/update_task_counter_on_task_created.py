from meiga import BoolResult
from petisco import event_handler, Event

from taskmanager.src.modules.tasks_count.application.tasks_count_increaser import (
    TasksCountIncreaser,
)


@event_handler()
def update_task_counter_on_task_created(event: Event) -> BoolResult:
    return TasksCountIncreaser.build().execute()
