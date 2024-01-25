"""
The module contains protocol classes.
"""

from typing import runtime_checkable, Protocol


@runtime_checkable
class Comparable(Protocol):
    """
    This protocol is intended for use with generic types that need
    to support ordering and equality comparisons.
    """

    def __eq__(self, other) -> bool:  # type: ignore[no-untyped-def]
        ...

    def __lt__(self, other) -> bool:  # type: ignore[no-untyped-def]
        ...
