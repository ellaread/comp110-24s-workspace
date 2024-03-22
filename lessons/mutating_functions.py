# Immutable: Cant be mutated or changed after creation
    # immutable types: int, float, bool, string, tuple
    # can be re-assigned, but not changed
# Mutable: can be mutated after creation 
    # mutable types: list and dict 
    # can be both reassigned and changed
    # can be mutated directly, but also with functions 
"""Practice with mutating functions."""
def remove_first(arg: list[str]) -> None:
    """Remove first element of input list."""
    arg.pop(0)

def get_first(arg: list[str]) -> str:
    """Return first element of arg without mutating."""
    return arg[0]

def get_and_remove_first(arg: list[str]) -> str:
    """Return first element AND remove it."""
    elem: str = arg[0]
    arg.pop(0)
    return elem