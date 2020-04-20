import os
from typing import Dict

from dataclasses import dataclass
from petisco.application.singleton import Singleton


@dataclass
class RabbitMQEnvConfig(metaclass=Singleton):
    user: str
    password: str
    host: str
    port: str
    mode: str
    topics: Dict

    def __init__(self):
        self.user = os.environ.get("RABBITMQ_USER", "guest")
        self.password = os.environ.get("RABBITMQ_PASSWORD", "guest")
        self.host = os.environ.get("RABBITMQ_HOST", "localhost")
        self.port = os.environ.get("RABBITMQ_PORT", "5672")
        self.topics = {"deploy": os.environ.get("RABBITMQ_DEPLOY_TOPIC", "deploy")}
