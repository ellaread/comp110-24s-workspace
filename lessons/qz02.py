
        
def jump(x: int) -> int:
    if x > 0:
        y: int = around(-1 * x)
        return y
    else:
        return x / 2
    
def around(x: int) -> int:
    x += 1
    if x > 0: 
        y: int = jump(x)
        return y
    else:
        return x * 2
    
x: int = 3
print(around(x))


def shrink(input: list[int]) -> list[int]:
    """Get values of list that are even and < 19."""
    i: int = 0
    shrunk: list[int] = []
    while i < len(input):
        if input[i] % 2 == 0 and input[i] < 19:
            shrunk.append(input[i])
        else:
            i += 1
    return shrunk