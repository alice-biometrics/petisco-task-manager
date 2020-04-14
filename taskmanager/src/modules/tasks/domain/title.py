from typing import Any

from meiga import Result, Failure, Error, Success
from petisco import (
    ValueObject,
    EmptyValueObjectError,
    ExceedLengthLimitValueObjectError,
)

LENGTH = 40


class Title(str, ValueObject):
    def __new__(cls, title, length=LENGTH):
        title = None if title == "None" else title
        cls.length = length
        return str.__new__(cls, title)

    def to_result(self) -> Result[Any, Error]:
        title = None if self == "None" else self

        if not title:
            return Failure(EmptyValueObjectError(self.__class__.__name__))

        if title is not None and len(title) > self.length:
            return Failure(ExceedLengthLimitValueObjectError(message=title))
        else:
            return Success(title)
