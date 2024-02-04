"""
Contains a FILO (First-In-Last-Out) stack implementation.
"""

import copy

from typing import Generic, List, Iterator, Optional, TypeVar

from .exceptions import EmptyCollectionException
from .protocols import Comparable


T = TypeVar("T", bound=Comparable)


class Stack(Generic[T]):
    """
    Represents a First-In-Last-Out (FILO) stack.
    """

    def __init__(self, values: Optional[List[T]] = None) -> None:
        """
        Initializes a new stack instance.
        """

        self._list: List[T] = [] if not values else values

    def __iter__(self) -> Iterator[T]:
        """
        Iterates through the stack.
        """

        yield from self._list

    def __getitem__(self, index: int) -> T:
        """
        Retrieve the element at the specified index from the stack.
        """

        return self._list[index]

    def __len__(self) -> int:
        """
        Returns the number of elements in the stack.
        """

        return len(self._list)

    @property
    def id(self) -> int:
        """
        Returns a unique identifier for this stack.
        """

        return id(self)

    def clear(self) -> None:
        """
        Removes all the elements from the stack.
        """

        self._list.clear()

    def contains(self, value: T) -> bool:
        """
        Returns `True` if the stack contains the specified value.
        """

        return value in self._list

    def copy(self) -> List[T]:
        """
        Returns a new list with the values from the stack.
        """

        return copy.deepcopy(self._list)

    def peek(self) -> Optional[T]:
        """
        Returns the object at the top of the stack without removing it.
        """

        if len(self) == 0:
            raise EmptyCollectionException("The stack is empty!")

        return self._list[-1]

    def pop(self) -> Optional[T]:
        """
        Removes and returns the object at the top of the stack.
        """

        if len(self) == 0:
            raise EmptyCollectionException("The stack is empty!")

        return self._list.pop()

    def push(self, value: T) -> None:
        """
        Inserts an object at the top of the stack.
        """

        self._list.append(value)
