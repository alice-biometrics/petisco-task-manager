from apscheduler.schedulers.background import BackgroundScheduler
from meiga import isSuccess
from petisco import (
    Event,
    Petisco,
    RabbitMQEventSubscriber,
    RabbitMqConnector,
    ConfigEventSubscriber,
    subscriber_handler,
)

TEN_MINUTES = 600  # seconds


@subscriber_handler()
def requeue_from_dead_letter(event: Event):
    publisher = Petisco.get_event_publisher()
    publisher.publish(event)
    return isSuccess


def subscribe_to_dead_letter():
    subscriber = RabbitMQEventSubscriber(
        connector=RabbitMqConnector(),
        subscribers={
            "dead-letter": ConfigEventSubscriber(
                organization="acme",
                service="taskmanager",
                topic="taskmanager-events",
                handler=requeue_from_dead_letter,
                dead_letter=True,
            )
        },
        connection_name="dead-letter-subscriber",
    )
    subscriber.start()

    scheduler = BackgroundScheduler()

    def shutdown():
        subscriber.start()
        scheduler.shutdown()

    scheduler.add_job(func=shutdown, trigger="interval", seconds=TEN_MINUTES)
    scheduler.start()
