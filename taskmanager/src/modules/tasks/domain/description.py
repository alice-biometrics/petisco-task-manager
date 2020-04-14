from typing import Any

from meiga import Result, Failure, Error, Success

from petisco.domain.value_objects.value_object import ValueObject
from petisco.domain.errors.input_exceed_lenght_limit_error import (
    InputExceedLengthLimitError,
)

LENGTH = 200


class Description(str, ValueObject):
    def __new__(cls, description, length=LENGTH):
        description = None if description == "None" else description
        cls.length = length
        return str.__new__(cls, description)

    def to_result(self) -> Result[Any, Error]:
        description = None if self == "None" else self

        if description is not None and len(description) > self.length:
            return Failure(InputExceedLengthLimitError(message=description))
        else:
            return Success(description)
