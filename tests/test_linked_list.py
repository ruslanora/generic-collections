"""
The module contains the LinkedList test case.
"""

# mypy: disable-error-code="union-attr"
# pylint: disable=missing-class-docstring,missing-function-docstring

import unittest

from src.datastructpy import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_first_and_last(self) -> None:
        ll = LinkedList[int]([1, 2, 3, 4, 5])

        self.assertIsNone(ll.first.prev)
        self.assertIsNone(ll.last.next)

    def test_add_first(self) -> None:
        ll = LinkedList[int]([1, 2, 3])
        ll.add_first(0)
        self.assertEqual(ll.first.value, 0)
        self.assertEqual(ll.first.next.value, 1)

    def test_add_last(self) -> None:
        ll = LinkedList[int]([1, 2, 3])
        ll.add_last(4)
        self.assertEqual(ll.last.value, 4)
        self.assertEqual(ll.last.prev.value, 3)

    def test_clear(self) -> None:
        ll = LinkedList[int]([1, 2, 3, 4, 5])
        self.assertEqual(len(ll), 5)
        ll.clear()
        self.assertEqual(len(ll), 0)
        self.assertEqual(ll.first, None)
        self.assertEqual(ll.last, None)

    def test_countains(self) -> None:
        ll = LinkedList[int]([1, 2, 3, 4, 5])
        self.assertFalse(ll.contains(0))
        self.assertTrue(ll.contains(1))
        ll.add_last(0)
        self.assertTrue(ll.contains(0))

    def test_find(self) -> None:
        ll = LinkedList[int]([1, 2, 3, 4, 5])
        self.assertIsNone(ll.find(6), None)
        self.assertIsNotNone(ll.find(5))
        self.assertEqual(ll.find(5).value, 5)

    def test_find_last(self) -> None:
        ll = LinkedList[int]([1, 2, 3, 4, 5])
        self.assertEqual(ll.find_last(4).prev.value, 3)
        self.assertEqual(ll.find_last(4).next.value, 5)

    def test_remove(self) -> None:
        ll = LinkedList[int]([1, 2, 3, 4, 5])
        self.assertEqual(ll.first.value, 1)
        ll.remove(1)
        self.assertEqual(ll.first.value, 2)

    def test_remove_first(self) -> None:
        ll = LinkedList[int]([1, 2, 3, 4, 5])
        self.assertEqual(ll.first.value, 1)
        self.assertEqual(len(ll), 5)
        ll.remove_first()
        self.assertEqual(ll.first.value, 2)
        self.assertEqual(len(ll), 4)

    def test_remove_last(self) -> None:
        ll = LinkedList[int]([1, 2, 3, 4, 5])
        self.assertEqual(ll.last.value, 5)
        self.assertEqual(len(ll), 5)
        ll.remove_last()
        self.assertEqual(ll.last.value, 4)
        self.assertEqual(len(ll), 4)


if __name__ == "__main__":
    unittest.main()
