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
        connection = RabbitMQEnvConfig.get_connection("publisher")
        return RabbitMQEventPublisher(
            connection=connection,
            organization="acme",
            service="taskmanager",
            topic="taskmanager-events",
        )

    event_publisher = NotImplementedEventPublisher()
    event_publisher_type = os.environ.get("EVENT_PUBLISHER_TYPE")
    if event_publisher_type and event_publisher_type == "rabbitmq":
        event_publisher = rabbitmq_event_publisher_provider()

    return event_publisher


def subscriber_provider(
    subscribers: Dict[str, ConfigEventSubscriber]
) -> IEventSubscriber:
    def rabbitmq_event_subscriber_provider() -> RabbitMQEventSubscriber:
        connection = RabbitMQEnvConfig.get_connection("subscriber")
        return RabbitMQEventSubscriber(connection=connection, subscribers=subscribers)

    event_subscriber = NotImplementedEventSubscriber(subscribers)
    event_subscriber_type = os.environ.get("EVENT_SUBSCRIBER_TYPE")
    if event_subscriber_type and event_subscriber_type == "rabbitmq":
        event_subscriber = rabbitmq_event_subscriber_provider()

    return event_subscriber
