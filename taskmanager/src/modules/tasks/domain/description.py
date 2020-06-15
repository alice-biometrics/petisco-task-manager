from meiga import Failure

from petisco import (
    EmptyValueObjectError,
    ExceedLengthLimitValueObjectError,
    StringValueObject,
)


class Description(StringValueObject):
    def guard(self):
        self._ensure_not_empty_value()
        self._ensure_value_is_less_than_200_char()

    def _ensure_not_empty_value(self):
        if self.value is None:
            raise Failure(EmptyValueObjectError(self.__class__.__name__))

    def _ensure_value_is_less_than_200_char(self):
        if len(self.value) > 200:
            raise ExceedLengthLimitValueObjectError(message=self.value)
