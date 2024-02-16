"""
Contains a min-heap-based priority queue.
"""

from typing import Generic, List, Optional, Tuple, TypeVar

from .base_comparer import BaseComparer, DefaultComparer
from .exceptions import EmptyCollectionException
from .protocols import Comparable


P = TypeVar("P", bound=Comparable)
T = TypeVar("T", bound=Comparable)


class PriorityQueue(Generic[P, T]):
    """
    Represents a min-heap-based priority queue.
    """

    def __init__(self) -> None:
        """
        Initializes a new priority queue.
        """

        self._comparer: Optional[BaseComparer[P]] = None
        self._heap: List[Tuple[P, T]] = []
        self._count: int = 0

    def __len__(self) -> int:
        """
        Returns the number of elements in the queue.
        """

        return self._count

    @property
    def comparer(self) -> BaseComparer[P]:
        """
        Returns the comparer used to evaluate equality of values.
        """

        if not self._comparer:
            self._comparer = DefaultComparer[P]()

        return self._comparer

    @comparer.setter
    def comparer(self, comparer: object) -> None:
        """
        Sets the custom comparer.
        """

        if not isinstance(comparer, BaseComparer):
            raise ValueError("Comparer should be an instance of BaseComparer.")

        self._comparer = comparer

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

        self._heap = []
        self._count = 0

    def dequeue(self) -> T:
        """
        Removes and returns the object at the beginning of the queue.
        """

        if not self._heap:
            raise EmptyCollectionException("The queue is empty!")

        self._swap(0, len(self._heap) - 1)
        _, value = self._heap.pop()
        self._heapify_down()
        self._count -= 1

        return value

    def enqueue(self, priority: P, value: T) -> None:
        """
        Adds an object to the end of the queue.
        """

        self._heap.append((priority, value))
        self._heapify_up(len(self._heap) - 1)
        self._count += 1

    def peek(self) -> T:
        """
        Returns the object at the beginning of the queue without removing it.
        """

        if not self._heap:
            raise EmptyCollectionException("The queue is empty!")

        return self._heap[0][1]

    def _heapify_up(self, index: int) -> None:
        """
        Moves the element at the given index up.
        """

        parent = (index - 1) // 2

        # pylint: disable-next=line-too-long
        if index > 0 and self.comparer.lt(self._heap[index][0], self._heap[parent][0]):
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index: int = 0) -> None:
        """
        Moves the element at the given index down.
        """

        child = 2 * index + 1

        if child >= len(self._heap):
            return

        right = child + 1

        if right < len(self._heap) and self.comparer.lt(
            self._heap[right][0], self._heap[child][0]
        ):
            child = right

        if self.comparer.lt(self._heap[child][0], self._heap[index][0]):
            self._swap(child, index)
            self._heapify_down(child)

    def _swap(self, i: int, j: int) -> None:
        """
        Swaps two elements in the internal heap list.
        """

        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
