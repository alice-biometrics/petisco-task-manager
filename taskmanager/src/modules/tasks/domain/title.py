from meiga import Failure
from petisco import (
    EmptyValueObjectError,
    ExceedLengthLimitValueObjectError,
    StringValueObject,
)


class Title(StringValueObject):
    def guard(self):
        self._ensure_value_contains_valid_char()
        self._ensure_not_empty_value()
        self._ensure_value_is_less_than_40_char()

    def _ensure_not_empty_value(self):
        if self.value is None:
            raise Failure(EmptyValueObjectError(self.__class__.__name__))

    def _ensure_value_is_less_than_40_char(self):
        if len(self.value) > 40:
            raise ExceedLengthLimitValueObjectError(message=self.value)
