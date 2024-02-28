"""Splitting a dictionary into two lists."""
__author__ = "730487065"


def get_keys(test: dict[str, int]) -> list[str]:
    """Return a list of all the keys in an imput dictionary."""
    key_list = []  # initializing empty list
    for key in test:
        key_list.append(key)
    return key_list


def get_values(test: dict[str, int]) -> list[int]:
    """Return a list of all values in a dictionary."""
    value_list = []  # initialize empty list for values.
    for value in test.values():
        value_list.append(value)  # Appending each value to value_list.
    return value_list