"""Demonstrate basic list syntax!"""

# Initialize an empty list
grocery_list: list[str] = list()  # ,- list constructor
grocery_list: list[str] = []  # <- literal

print(grocery_list)
# add item to list
grocery_list.append("bananas")
# method: a function that belongs to the list class, like calling append(grocery_list, "bananas")
grocery_list.append("milk")
grocery_list.append("bread")
print("After appending: ")
print(grocery_list)

# initializing an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print("Populated list: ")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

# indexing (start at 0 like with strings)
print("Print first element of string")
print(grocery_list[0])

# modifying by index 
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change: ")
print(grocery_list)

# you can have duplicates 
grocery_list.append("almond milk")
print("Add almond milk again: ")
print(grocery_list)

# length of a list
print("Length of list: ")
print(len(grocery_list))

# remove an item from a list
grocery_list.pop(1)
print("After removing almond milk: ")
print(grocery_list)

#Lists and Functions
#Functions can take lists as arguments, return or create lists, and modify lists!

# Function name: display
# Parameter: list[str]
# return Nothing:
# print out the list!
print("~*~ Functions! ~*~")
def display(word: list[str]):
    print(word)

display(grocery_list)
x = display(["Alyssa", "Erin", "AK"])
print(x)

# Create a list!
# name: create
# parameters str and str
# RV: list[str]
# put both parameters into list and return that list
def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

print(create("ella", "grayson"))
