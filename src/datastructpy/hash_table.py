"""
HashTable implementation using separate chaining to resolve collisions.
"""

from typing import List, Generic, Iterator, Tuple, Optional, TypeVar

from .protocols import Comparable


T = TypeVar("T", bound=Comparable)


class HashTable(Generic[T]):
    """
    Represents a hash table.
    """

    def __init__(self, capacity: int = 32) -> None:
        """
        Initializes the hash table with a given number of buckets.
        """

        self._buckets: List[List[Tuple[str, T]]] = [[] for _ in range(capacity)]
        self._count: int = 0

    def __iter__(self) -> Iterator[T]:
        """
        Iterates over all values stored in the hash table.
        """

        for bucket in self._buckets:
            for _, value in bucket:
                yield value

    def __len__(self) -> int:
        """
        Returns the number of stored in the hash table.
        """

        return self._count

    @property
    def capacity(self) -> int:
        """
        Returns the capacity of the hash table.
        """

        return len(self._buckets)

    def add(self, key: str, value: T) -> None:
        """
        Adds a key-value pair to the hash table.
        Updates the value if the key already exists.
        """

        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._count += 1

    def contains(self, key: str) -> bool:
        """
        Checks whether a key exists in the hash table.
        """

        return bool(self.find(key))

    def clear(self) -> None:
        """
        Removes all the elements from the hash table.
        """

        for bucket in self._buckets:
            bucket.clear()

        self._count = 0

    def find(self, key: str) -> Optional[T]:
        """
        Returns the value associated with the given key.
        """

        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key: str) -> None:
        """
        Removes the key-value pair associated with the given key.
        """

        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return

        raise KeyError(f"'{key}' not found.")

    def _hash(self, key: str) -> int:
        """
        Computes a hash index for the given key.
        """

        hash_sum = sum(ord(char) for char in key)
        return hash_sum % len(self._buckets)
