"""Define functions and variables that I'll be importing."""

def add(x: int, y: int) -> int: 
    return x + y

if __name__ == "__main__":
    print(add(1,2))

def double(x: int) -> int:
    return x * 2

def double_display(y: int):
    print(y * 2)

double_display(2)
    
if __name__ == "__main__":
    print(double(3))