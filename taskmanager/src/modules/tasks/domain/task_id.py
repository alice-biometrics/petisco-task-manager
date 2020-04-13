import base64
import os
from typing import Any

from meiga import Result, Failure, Error, Success

from petisco.domain.value_objects.value_object import ValueObject
from petisco.domain.errors.input_exceed_lenght_limit_error import (
    InputExceedLengthLimitError,
)

LENGTH = 16


class TaskId(str, ValueObject):
    def __new__(cls, task_id, length=LENGTH):
        task_id = None if task_id == "None" else user_id
        cls.length = length
        return str.__new__(cls, task_id)

    def to_result(self) -> Result[Any, Error]:
        task_id = None if self == "None" else self

        if task_id is not None and len(task_id) > self.length:
            return Failure(InputExceedLengthLimitError(message=task_id))
        else:
            return Success(user_id)

    @staticmethod
    def generate():
        r = os.urandom(LENGTH)
        return TaskId(base64.b64encode(r, altchars=b"-_").decode("utf-8")[:LENGTH])
