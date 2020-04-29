import os
from typing import Dict

from petisco import (
    IEventPublisher,
    RabbitMQEventPublisher,
    NotImplementedEventPublisher,
    RabbitMQEnvConfig,
    IEventSubscriber,
    ConfigEventSubscriber,
    RabbitMQEventSubscriber,
    NotImplementedEventSubscriber,
)


def publisher_provider() -> IEventPublisher:
    def rabbitmq_event_publisher_provider() -> RabbitMQEventPublisher:
        connection = RabbitMQEnvConfig.get_connection()
        return RabbitMQEventPublisher(
            connection=connection,
            organization="acme",
            service="taskmanager",
            topic="taskmanager-events",
        )

    event_publisher_type = os.environ.get("EVENT_PUBLISHER_TYPE")
    if not event_publisher_type:
        return NotImplementedEventPublisher()
    elif event_publisher_type == "rabbitmq":
        return rabbitmq_event_publisher_provider()


def subscriber_provider(
    subscribers: Dict[str, ConfigEventSubscriber]
) -> IEventSubscriber:
    def rabbitmq_event_subscriber_provider() -> RabbitMQEventSubscriber:
        connection = RabbitMQEnvConfig.get_connection()
        return RabbitMQEventSubscriber(connection=connection, subscribers=subscribers)

    event_subscriber_type = os.environ.get("EVENT_SUBSCRIBER_TYPE")
    if not event_subscriber_type:
        return NotImplementedEventSubscriber(subscribers)
    elif event_subscriber_type == "rabbitmq":
        return rabbitmq_event_subscriber_provider()
