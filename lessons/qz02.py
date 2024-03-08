
        
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


