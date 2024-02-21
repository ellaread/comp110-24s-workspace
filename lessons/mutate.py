"""Mutating functions."""
__author__ = "730487065"


def manual_append(first: list[int], second: int) -> None:
    """Appending lists function."""
    first.append(second)


def double(func1: list[int]) -> None: 
    """Doubling the original list function."""
    index = 0
    while index < len(func1):
        func1[index] *= 2
        index += 1