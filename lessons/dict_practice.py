"""Practice with dictionaries!"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
# adding
print("After adding mint.")
print(ice_cream)
#removing
ice_cream.pop("mint")
print("After removing mint.")
# or
# ice_cream: dict[str, int] = dict()
# you can use single quotes in dictionaries as well as ""
print(ice_cream)

#accessing
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# updating a value
ice_cream["vanilla"] += 1
print("after adding one vanilla")
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")
print(len(ice_cream))


# checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)

courses: dict[int, str] = dict()
courses[110] = "Intro to Programming"
courses[210] = "Data Structures"

print(courses[110])

points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100
print(points)

print(ice_cream["pecan"])