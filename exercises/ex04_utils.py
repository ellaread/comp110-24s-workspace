"""Exercise to practice lists."""
__author__ = "730487065"


def all(arg_one: list[int], arg_two: int) -> bool:
    """Finding out if all the integers in a list are the same as the target number."""
    if not arg_one:   # this line makes sure list is not empty
        return False
    num_idx: int = 0   # index
    while num_idx <= (len(arg_one) - 1):   # while index is less than len-1 
        if arg_one[num_idx] != arg_two:   # if current index isnt equal to target
            return False
        num_idx += 1   # update index
    return True   # if we get here, all indexes of list match target num


def max(input: list[int]) -> int:
    """Determining the highest number in a list of numbers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    num_idx: int = 0 
    highinput: int = input[0]
    while num_idx < (len(input)):
        if input[num_idx] > highinput:
            highinput = input[num_idx]
        num_idx += 1
    return highinput


def is_equal(lista: list[int], listb: list[int]) -> bool:
    """Checking if each list is exactly the same."""
    if len(lista) != len(listb):  # making sure both lists are the same length
        return False
    idx: int = 0
    while idx < len(lista):
        if lista[idx] != listb[idx]:  # making sure each number and location of the number in each list matches 
            return False
        idx += 1
    return True


def extend(lista: list[int], listb: list[int]) -> None:
    """Extending functions."""
    lista += listb