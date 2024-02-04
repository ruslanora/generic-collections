"""
The module contains the Queue test case.
"""

# pylint: disable=missing-class-docstring,missing-function-docstring

import unittest

from src.datastructpy import Queue


class TestQueue(unittest.TestCase):
    def test_count(self) -> None:
        q = Queue[int]([1, 2, 3, 4, 5])
        self.assertEqual(len(q), 5)
        q.enqeue(6)
        q.enqeue(7)
        self.assertEqual(len(q), 7)
        q.dequeue()
        self.assertEqual(len(q), 6)

    def test_clear(self) -> None:
        q = Queue[int]([1, 2, 3, 4, 5])
        self.assertEqual(len(q), 5)
        q.clear()
        self.assertEqual(len(q), 0)

    def test_contains(self) -> None:
        q = Queue[int]([1, 2, 3, 4, 5])
        self.assertFalse(q.contains(6))
        q.enqeue(6)
        self.assertTrue(q.contains(6))

    def test_copy(self) -> None:
        ll = [1, 2, 3, 4, 5]
        q = Queue[int](ll)
        self.assertNotEqual(id(ll), id(q.copy()))

    def test_dequeue(self) -> None:
        q = Queue[int]([1, 2, 3, 4, 5])
        self.assertTrue(q.contains(1))
        v = q.dequeue()
        self.assertEqual(v, 1)
        self.assertFalse(q.contains(1))
        self.assertEqual(q[0], 2)

    def test_enqueue(self) -> None:
        q = Queue[int]([1, 2, 3, 4, 5])
        self.assertFalse(q.contains(6))
        q.enqeue(6)
        self.assertTrue(q.contains(6))
        self.assertEqual(q[-1], 6)

    def test_peek(self) -> None:
        q = Queue[int]([1, 2, 3, 4, 5])
        v = q.dequeue()
        self.assertEqual(v, 1)
        self.assertFalse(q.contains(1))
        self.assertEqual(q[0], 2)


if __name__ == "__main__":
    unittest.main()
