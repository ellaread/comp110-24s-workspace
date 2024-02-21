"""example functions to learn definitions and calling syntax"""

def my_max(num1: int, num2: int) -> int: 
    """Returns the maximum value out of two numbers"""
    if num1 >= num2:
        return num1
    else: #number1 < number 2
        return num2
    return 0 
    
max: int = my_max(1,10)
other_max: int = my_max(11,3)
print(other_max)

def view(my_list: list[str]):
    idx: int = 0
    while idx < len(my_list):
        print(my_list[idx])
        idx += 1

msg: list[str] = ["Hello", "World"]
view(msg)

def lessen(my_list: list[str]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1

msg: list[str] = [4, 5, 6]
lessen(msg)