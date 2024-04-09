"""Challenge Question Writing a Recursive Function."""
__author__ = "730487065"


def f(n: int, k: int) -> int:
    """Recursive function example."""
    if n == 0:  # Base case
        return 0
    else:  # Recursive rule
        return f(n - 1, k) + k
    

print(f(2,3))