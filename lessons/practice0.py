x: int = 10
result:str = ""
 
while x > 0:
    if x % 3 == 0:
        result = result + str(x)
    else:
        result = str(x) + result
    x = x // 2
print(result)

age: int = int(input("What is your age?"))
if age <= 12:
    price: int = 5
elif age > 60:
    price: int = 5
else:
    price: int = 10
print(price)