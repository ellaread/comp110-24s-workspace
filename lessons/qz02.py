"""Practicing for quiz 2."""
def odd_and_even(name: list[int]) -> list[int]:
    """Find the odd elements in the list with an even index"""
    oddeven_list: list[int] = []  # initializing empty list
    i: int = 0
    while i < len(name):
        if name[i] % 2 == 1 and i % 2 == 0:
            oddeven_list.append(name[i])
        i += 1
    return oddeven_list

def value_exists(value_one: dict[str, int], value_two: int) -> bool:
    """determining if a given value exists in a dictionary."""
    exists: bool = False
    for elem in value_one:
        if value_one[elem] == value_two:
            exists = True
    return exists

def short_words(my_list: list[str]) -> list[str]:
    """Returns lis of words that are shorter than 5 characters."""
    new_list: list[str] = []
    for x in my_list:
        if len(x) < 5:
            new_list.append(x)
        else:
            print(f"{x} is too long!")
    return new_list
