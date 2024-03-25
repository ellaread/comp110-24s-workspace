"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sort_index = 0
    while sort_index < len(x) - 1: 
        unsort_index = sort_index + 1 
        while unsort_index > 0 and x[unsort_index] < x[unsort_index - 1]:
            x[unsort_index], x[unsort_index - 1] = x[unsort_index - 1], x[unsort_index]
            unsort_index -= 1 
        sort_index += 1 
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
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
        counter += 1 
    print(x)
    return None

    