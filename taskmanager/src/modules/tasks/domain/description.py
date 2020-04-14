from typing import Any

from meiga import Result, Failure, Error, Success

from petisco import (
    ValueObject,
    EmptyValueObjectError,
    ExceedLengthLimitValueObjectError,
)


LENGTH = 200


class Description(str, ValueObject):
    def __new__(cls, description, length=LENGTH):
        description = None if description == "None" else description
        cls.length = length
        return str.__new__(cls, description)

    def to_result(self) -> Result[Any, Error]:
        description = None if self == "None" else self

        if not description:
            return Failure(EmptyValueObjectError(self.__class__.__name__))

        if description is not None and len(description) > self.length:
            return Failure(ExceedLengthLimitValueObjectError(message=description))
        else:
            return Success(description)
