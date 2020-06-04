from os import environ

from petisco import INotifier
from petisco.notifier.config.config_notifier import (
    get_slack_notifier,
    get_default_notifier,
)


def notifier_provider() -> INotifier:
    notifier = environ.get("NOTIFIER")
    if notifier == "default":
        return get_default_notifier()
    else:
        return get_slack_notifier()
