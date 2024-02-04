"""
The module contains the Stack test case.
"""

# pylint: disable=missing-class-docstring,missing-function-docstring

import unittest

from src.datastructpy import Stack


class TestStack(unittest.TestCase):
    def test_count_and_push(self) -> None:
        s = Stack[int]([1, 2, 3, 4])
        self.assertEqual(len(s), 4)
        s.push(5)
        s.push(6)
        self.assertEqual(len(s), 6)

    def test_clear(self) -> None:
        s = Stack[int]([1, 2, 3, 4, 5])
        self.assertEqual(len(s), 5)
        s.clear()
        self.assertEqual(len(s), 0)
        with self.assertRaises(IndexError):
            # pylint: disable=pointless-statement
            s[0]

    def test_contains(self) -> None:
        s = Stack[int]([1, 2, 3, 4, 5])
        self.assertFalse(s.contains(6))
        s.push(6)
        self.assertTrue(s.contains(6))

    def copy(self) -> None:
        arr = [1, 2, 3, 4, 5]
        s = Stack[int](arr)
        c = s.copy()
        self.assertEqual(c, arr)
        self.assertNotEqual(id(c), id(arr))

    def peek(self) -> None:
        s = Stack[int]([1, 2, 3, 4, 5])
        self.assertEqual(5, s.pop())
        self.assertTrue(s.contains(5))

    def test_pop(self) -> None:
        s = Stack[int]([1, 2, 3, 4, 5])
        self.assertEqual(5, s.pop())
        self.assertFalse(s.contains(5))


if __name__ == "__main__":
    unittest.main()
