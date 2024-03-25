"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""

    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    x = [7, 3, 8, 5, 2, 4]
    counter = 0
    while counter < len(x):
        min_idx = counter
        secondary_counter = counter + 1 
        while secondary_counter < len(x): 
            if x[secondary_counter] < x[min_idx]:
                min_idx = secondary_counter
            secondary_counter += 1 
        if min_idx != counter: 
            temporary_int = x[counter]
            x[counter] = x[min_idx]
            x[min_idx] = temporary_int
        counter =+ 1 
    return None
    