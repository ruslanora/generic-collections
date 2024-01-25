"""
This module contains an implementation of a doubly linked list.
"""

# pylint: disable=protected-access

from typing import final, Any, List, Generic, Iterator, Optional, TypeVar

from .base_comparer import BaseComparer, DefaultComparer
from .exceptions import EmptyCollectionException
from .protocols import Comparable


T = TypeVar("T", bound=Comparable)


@final
class LinkedListNode(Generic[T]):
    """
    Represents a node in a doubly linked list.
    """

    # pylint: disable-next=line-too-long
    def __init__(self, value: T, linked_list: Optional["LinkedList[T]"] = None) -> None:
        """
        Initializes a new node with a given value.
        """

        self._list: Optional["LinkedList[T]"] = linked_list
        self._next: Optional["LinkedListNode[T]"] = None
        self._prev: Optional["LinkedListNode[T]"] = None

        self.value: T = value

    def __eq__(self, other) -> bool:  # type: ignore[no-untyped-def]
        """
        Checks equality between two objects.
        """

        if isinstance(other, LinkedListNode):
            return id(self) == id(other)
        return False

    def __del__(self) -> None:
        """
        Removes all the references from the node.
        """

        self._list = None
        self._next = None
        self._prev = None

    @property
    def list(self) -> Optional["LinkedList[T]"]:
        """
        Returns a linked list the node belongs to, or `None`
        if the node is not linked.
        """

        return self._list

    @property
    def next(self) -> Optional["LinkedListNode[T]"]:
        """
        Returns the next node in the linked list, or `None`
        if there is no next node.
        """

        # pylint: disable-next=protected-access
        if self._list and self._list._head == self._next:
            return None

        return self._next

    @property
    def prev(self) -> Optional["LinkedListNode[T]"]:
        """
        Returns the previous node in the linked list, or `None`
        if there is no previous node.
        """

        # pylint: disable-next=protected-access
        if self._list and self._list._head == self:
            return None

        return self._prev


class LinkedList(Generic[T]):
    """
    Represents a doubly linked list.
    """

    def __init__(self, values: Optional[List[T]] = None) -> None:
        """
        Initializes a new linked list instance.
        """

        self._head: Optional[LinkedListNode[T]] = None
        self._comparer: Optional[BaseComparer[T]] = None
        self._count: int = 0

        if values:
            for value in values:
                self.add_last(value)

    def __iter__(self) -> Iterator[LinkedListNode[T]]:
        """
        Iterates through the list.
        """

        node = self._head

        while node:
            yield node
            node = node.next

    def __eq__(self, other: Any) -> bool:
        """
        Description.
        """

        if not isinstance(other, LinkedList):
            return False
        return id(self) == id(other)

    def __len__(self) -> int:
        """
        Returns the number of nodes stored in the list.
        """

        return self._count

    @property
    def id(self) -> int:
        """
        Returns a unique identifier for this linked
        list based on its memory address.
        """

        return id(self)

    @property
    def comparer(self) -> BaseComparer[T]:
        """
        Returns the comparer used to evaluate equality of values.
        """

        if not self._comparer:
            self._comparer = DefaultComparer[T]()

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
    def first(self) -> Optional[LinkedListNode[T]]:
        """
        Returns the first node of the list, or `None` if the list is empty.
        """

        return self._head

    @property
    def last(self) -> Optional[LinkedListNode[T]]:
        """
        Returns the last node of the list, or `None` if the list is empty.
        """

        if self._head and self._head._prev:
            return self._head._prev

        return None

    def add_first(self, value: T) -> LinkedListNode[T]:
        """
        Adds a new node to the beginning of the list.
        """

        node = LinkedListNode[T](value, self)

        if not self._head:
            self._add_to_empty_list(node)
        else:
            self._add_node_before(self._head, node)
            self._head = node

        return node

    def add_last(self, value: T) -> LinkedListNode[T]:
        """
        Adds a new node to the end of the list.
        """

        node = LinkedListNode[T](value, self)

        if not self._head:
            self._add_to_empty_list(node)
        else:
            self._add_node_before(self._head, node)

        return node

    def clear(self) -> None:
        """
        Removes all elements from the list.
        """

        for node in self:
            del node

        self._count = 0
        self._head = None

    def contains(self, value: T) -> bool:
        """
        Returns `True` if the list contains the specified value.
        """

        return bool(self.find(value))

    def find(self, value: T) -> Optional[LinkedListNode[T]]:
        """
        Returns the first node containing the specified value,
        or `None` if not found.
        """

        for node in self:
            if self.comparer.eq(node.value, value):
                return node

        return None

    def find_last(self, value: T) -> Optional[LinkedListNode[T]]:
        """
        Returns the last node containing the specified value,
        or `None` if not found.
        """

        if not self._head:
            return None

        last = self._head._prev
        node = last

        if node:
            while True:
                # pylint: disable-next=line-too-long
                if self.comparer.eq(node.value, value):  # type: ignore[union-attr]
                    return node

                node = node._prev  # type: ignore[union-attr]

                if node == last:
                    break

        return None

    def remove(self, value: T) -> None:
        """
        Removes the first node with the specified value from the list.
        """

        for node in self:
            if self.comparer.eq(node.value, value):
                self._remove_node(node)
                break

    def remove_first(self) -> None:
        """
        Removes the first node from the list.
        """

        if not self._head:
            raise EmptyCollectionException("The list is empty!")

        self._remove_node(self._head)

    def remove_last(self) -> None:
        """
        Removes the last node from the list.
        """

        if not self._head:
            raise EmptyCollectionException("The list is empty!")

        if self._head and self._head._prev:
            self._remove_node(self._head._prev)

    def to_list(self) -> list[T]:
        """
        Returns a standard Python list of the node values.
        """

        result: list[T] = []

        for node in self:
            result.append(node.value)

        return result

    def _add_node_before(
        self, node: LinkedListNode[T], new_node: LinkedListNode[T]
    ) -> None:
        """
        Adds a new node before the specified node in the list.
        """

        new_node._next = node
        new_node._prev = node._prev

        if node._prev and node._prev._next:
            node._prev._next = new_node

        node._prev = new_node

        self._count += 1

    def _add_to_empty_list(self, node: LinkedListNode[T]) -> None:
        """
        Adds a new node to an empty list.
        """

        node._next = node
        node._prev = node
        self._head = node
        self._count += 1

    def _remove_node(self, node: LinkedListNode[T]) -> None:
        """
        Removes a node from the list and updates links accordingly.
        """

        if node._next == node:
            self._head = None
        else:
            if node._next:
                node._next._prev = node._prev

            if node._prev:
                node._prev._next = node._next

            if self._head == node:
                self._head = node._next

        del node

        self._count -= 1

    def _validate_node(self, node: LinkedListNode[T]) -> None:
        """
        Validates that the node belongs to this list.
        """

        if not node._list or self != node._list:
            raise ValueError("The node does not belong to this list.")
