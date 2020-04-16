import os

from petisco import IEventManager, NotImplementedEventManager, RabbitMQEventManager
from pika import PlainCredentials, ConnectionParameters

from taskmanager.src.config.config_event_manager import RabbitMQEnvConfig


def event_manager_provider() -> IEventManager:
    event_manager_type = os.environ.get("EVENT_MANAGER_TYPE")
    if not event_manager_type:
        return NotImplementedEventManager()
    elif event_manager_type == "rabbitmq":
        return rabbitmq_event_manager_provider()


def rabbitmq_event_manager_provider() -> IEventManager:
    config_rabbitmq = RabbitMQEnvConfig()
    credentials = PlainCredentials(
        username=config_rabbitmq.user, password=config_rabbitmq.password
    )
    return RabbitMQEventManager(
        connection_parameters=ConnectionParameters(
            host=config_rabbitmq.host,
            port=config_rabbitmq.port,
            credentials=credentials,
        ),
        subscribers=None,
    )
