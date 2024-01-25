"""
The comparer module for generic value comparison operations.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .protocols import Comparable


T = TypeVar("T", bound=Comparable)


class BaseComparer(ABC, Generic[T]):
    """
    Abstract base class for value comparison.
    """

    @abstractmethod
    def eq(self, value1: T, value2: T) -> bool:
        """
        Should check if value1 is equal to value2.
        """

    @abstractmethod
    def lt(self, value1: T, value2: T) -> bool:
        """
        Should check if value1 is less than value2.
        """

    def lte(self, value1: T, value2: T) -> bool:
        """
        Checks if value1 is less than or equal to value2.
        """

        return value1 < value2 or value1 == value2

    def gte(self, value1: T, value2: T) -> bool:
        """
        Checks if value1 is greater than or equal to value2.
        """

        return value1 > value2 or value1 == value2

    def gt(self, value1: T, value2: T) -> bool:
        """
        Checks if value1 is greater than value2.
        """

        return value1 > value2


class DefaultComparer(BaseComparer[T]):
    """
    Default implementation of the BaseComparer interface.
    """

    def eq(self, value1: T, value2: T) -> bool:
        return value1 == value2

    def lt(self, value1: T, value2: T) -> bool:
        return value1 < value2
