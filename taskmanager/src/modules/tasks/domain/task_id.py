import base64
import os
from typing import Any

from meiga import Result, Failure, Error, Success
from petisco import (
    ValueObject,
    EmptyValueObjectError,
    ExceedLengthLimitValueObjectError,
)


LENGTH = 16


class TaskId(str, ValueObject):
    def __new__(cls, task_id, length=LENGTH):
        task_id = None if task_id == "None" else task_id
        cls.length = length
        return str.__new__(cls, task_id)

    def to_result(self) -> Result[Any, Error]:
        task_id = None if self == "None" else self

        if not task_id:
            return Failure(EmptyValueObjectError(self.__class__.__name__))

        if task_id is not None and len(task_id) > self.length:
            return Failure(ExceedLengthLimitValueObjectError(message=task_id))
        else:
            return Success(task_id)

    @staticmethod
    def generate():
        r = os.urandom(LENGTH)
        return TaskId(base64.b64encode(r, altchars=b"-_").decode("utf-8")[:LENGTH])
