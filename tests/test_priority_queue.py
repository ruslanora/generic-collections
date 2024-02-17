"""
The module contains the PriorityQueue test case.
"""

# pylint: disable=missing-class-docstring,missing-function-docstring


import unittest

from src.datastructpy import EmptyCollectionException, PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = PriorityQueue[int, str]()

    def test_enqueue_and_peek(self) -> None:
        self.queue.enqueue(3, "low")
        self.queue.enqueue(1, "high")
        self.queue.enqueue(2, "medium")
        self.assertEqual(self.queue.peek(), "high")

    def test_dequeue(self) -> None:
        self.queue.enqueue(3, "low")
        self.queue.enqueue(1, "high")
        self.queue.enqueue(2, "medium")
        self.assertEqual(self.queue.dequeue(), "high")
        self.assertEqual(self.queue.dequeue(), "medium")
        self.assertEqual(self.queue.dequeue(), "low")

    def test_dequeue_empty_queue(self) -> None:
        with self.assertRaises(EmptyCollectionException):
            self.queue.dequeue()

    def test_peek_empty_queue(self) -> None:
        with self.assertRaises(EmptyCollectionException):
            self.queue.peek()

    def test_clear(self) -> None:
        self.queue.enqueue(3, "low")
        self.queue.enqueue(1, "high")
        self.queue.clear()

        self.assertEqual(len(self.queue), 0)

    def test_len(self) -> None:
        self.queue.enqueue(3, "low")
        self.queue.enqueue(1, "high")
        self.queue.enqueue(2, "medium")
        self.assertEqual(len(self.queue), 3)

    def test_priority_order(self) -> None:
        self.queue.enqueue(5, "low")
        self.queue.enqueue(1, "high")
        self.queue.enqueue(10, "medium")
        self.assertEqual(self.queue.dequeue(), "high")
        self.assertEqual(self.queue.dequeue(), "low")
        self.assertEqual(self.queue.dequeue(), "medium")


if __name__ == "__main__":
    unittest.main()
