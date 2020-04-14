import base64
import os
from typing import Any

from meiga import Result, Failure, Error, Success

from petisco.domain.value_objects.value_object import ValueObject
from petisco.domain.errors.input_exceed_lenght_limit_error import (
    InputExceedLengthLimitError,
)

LENGTH = 40


class Title(str, ValueObject):
    def __new__(cls, title, length=LENGTH):
        title = None if title == "None" else title
        cls.length = length
        return str.__new__(cls, title)

    def to_result(self) -> Result[Any, Error]:
        title = None if self == "None" else self

        if title is not None and len(title) > self.length:
            return Failure(InputExceedLengthLimitError(message=title))
        else:
            return Success(title)
