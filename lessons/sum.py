"""Summing the elements of a list using different loops."""
__author__ = "730487065"


def w_sum(vals: list[float]) -> float:
    """Using while loops to find the sum of a set of numbers."""
    index = 0
    sum = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Using for loops to find sums of sets."""
    sum = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Using for loops with range to find sum of sets."""
    sum = 0.0
    for elem in range(len(vals)):
        sum += vals[elem]
    return sum