from petisco import Petisco, LogMessage, INFO


def recurring_task():
    Petisco.get_logger().log(INFO, LogMessage().set_message("recurring_task"))


def scheduled_task():
    Petisco.get_logger().log(INFO, LogMessage().set_message("scheduled_task"))


def instant_task():
    Petisco.get_logger().log(INFO, LogMessage().set_message("instant_task"))
