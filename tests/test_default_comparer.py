"""
The module contains the DefaultComparer test case.
"""

# pylint: disable=missing-class-docstring,missing-function-docstring

import unittest

from src.datastructpy import DefaultComparer


class TestDefaultComparer(unittest.TestCase):
    def setUp(self) -> None:
        self.comparer = DefaultComparer[int]()

    def test_eq(self) -> None:
        self.assertTrue(self.comparer.eq(5, 5))
        self.assertFalse(self.comparer.eq(5, 3))

    def test_gt(self) -> None:
        self.assertTrue(self.comparer.gt(5, 3))
        self.assertFalse(self.comparer.gt(5, 5))
        self.assertFalse(self.comparer.gt(5, 8))

    def test_gte(self) -> None:
        self.assertTrue(self.comparer.gte(5, 3))
        self.assertTrue(self.comparer.gte(5, 5))
        self.assertFalse(self.comparer.gte(5, 8))

    def test_lt(self) -> None:
        self.assertFalse(self.comparer.lt(5, 3))
        self.assertFalse(self.comparer.lt(5, 5))
        self.assertTrue(self.comparer.lt(5, 8))

    def test_lte(self) -> None:
        self.assertFalse(self.comparer.lte(5, 3))
        self.assertTrue(self.comparer.lte(5, 5))
        self.assertTrue(self.comparer.lte(5, 8))


if __name__ == "__main__":
    unittest.main()
