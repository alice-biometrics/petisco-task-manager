from typing import Optional

from onboardingrest.src.kyc.domain.entities.device.device_info import DeviceInfo
from petisco import use_case_handler, ApplicationConfig, UseCase, Name, IEventManager

from meiga import Result, Error, Failure, Success

from onboardingrest.application_setup import ONBOARDING_TOPIC
from onboardingrest.src.kyc.domain.entities.device.email import Email
from onboardingrest.src.kyc.domain.events.user_created import UserCreated
from onboardingrest.src.kyc.domain.services.auth.interface_auth_service import (
    IAuthService,
)
from petisco import InfoId
from onboardingrest.src.shared.domain.repositories.interface_user_repository import (
    IUserRepository,
)


@use_case_handler(
    logging_parameters_whitelist=["info_id"]
)
class CreateTask(UseCase):
    def __init__(self, task_repository: ITaskRepository, event_manager: IEventManager):
        self.task_repository = task_repository
        self.event_manager = event_manager

    def execute(self, task_id: TaskId) -> Result[str, Error]:
        task = Task.create()
        self.task_repository.save(task).unwrap_or_return()
        self.event_manager.publish_list(task.pull_domain_events())
        return isSuccess
