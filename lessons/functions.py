"""Demonstrates functions"""
from random import randint

y: str = print("Hello!")
print(y)

x: int = round(10.25)
print(x)

z: int = randint(1,7)
print(z)

def my_max(a: int, b: int) -> int:
   """Returns the largest argument."""
   if a >= b:
      return a

   return b


print(my_max(10, 0))