"""
Contains a FIFO (First-In-First-Out) queue implementation.
"""

import copy

from typing import Generic, List, Iterator, Optional, TypeVar

from .exceptions import EmptyCollectionException
from .protocols import Comparable


T = TypeVar("T", bound=Comparable)


class Queue(Generic[T]):
    """
    Represents a FIFO (First-In-First-Out) queue.
    """

    def __init__(self, values: Optional[List[T]] = None) -> None:
        """
        Initializes a new queue instance.
        """

        self._list: List[T] = [] if not values else values

    def __iter__(self) -> Iterator[T]:
        """
        Iterates through the queue.
        """

        yield from self._list

    def __len__(self) -> int:
        """
        Returns the number of elements in the queue.
        """

        return len(self._list)

    def __getitem__(self, index: int) -> T:
        """
        Retrieve the element at the specified index from the queue.
        """

        return self._list[index]

    @property
    def id(self) -> int:
        """
        Returns a unique identifier for this queue.
        """

        return id(self)

    def clear(self) -> None:
        """
        Removes all the elements from the queue.
        """

        self._list.clear()

    def contains(self, value: T) -> bool:
        """
        Returns `True` if the queue contains the specified value.
        """

        return value in self._list

    def copy(self) -> List[T]:
        """
        Returns a new list with the values from the queue.
        """

        return copy.deepcopy(self._list)

    def dequeue(self) -> Optional[T]:
        """
        Removes and returns the object at the beginning of the queue.
        """

        if len(self) == 0:
            raise EmptyCollectionException("The queue is empty!")

        return self._list.pop(0)

    def enqeue(self, value: T) -> None:
        """
        Adds an object to the end of the queue.
        """

        self._list.append(value)

    def peek(self) -> Optional[T]:
        """
        Returns the object at the beginning of the queue without removing it.
        """

        if len(self) == 0:
            raise EmptyCollectionException("The queue is empty!")

        return self._list[0]
