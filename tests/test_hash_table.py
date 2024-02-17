"""
The module contains a test case for HashTable.
"""

# pylint: disable=missing-class-docstring,missing-function-docstring

import unittest

from src.datastructpy import HashTable


class TestHashTable(unittest.TestCase):
    def test_count(self) -> None:
        table = HashTable[int]()
        table.add("hello", 1)
        self.assertEqual(len(table), 1)
        table.add("world", 2)
        self.assertEqual(len(table), 2)
        table.remove("hello")
        self.assertEqual(len(table), 1)

    def test_add_and_contains(self) -> None:
        table = HashTable[int]()
        table.add("hello", 1)
        self.assertTrue(table.contains("hello"))
        self.assertFalse(table.contains("world"))
        table.add("world", 2)
        self.assertTrue(table.contains("world"))

    def test_find_and_remove(self) -> None:
        table = HashTable[int]()
        table.add("hello", 1)
        table.add("world", 2)

        value = table.find("hello")
        self.assertEqual(value, 1)

        value = table.find("!")
        self.assertIsNone(value)

        table.remove("hello")
        self.assertIsNone(table.find("hello"))


if __name__ == "__main__":
    unittest.main()
