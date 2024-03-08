"""Dictionary Utils Exercise!"""
__author__ = "730487065"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """This is a function that inverts keys and values in a dictionary."""
    output_dict = {}  # initializing empty dictionary
    for key in input_dict:
        value = input_dict[key]
        if value in output_dict:
            raise KeyError("Duplicate value found while inverting the dictionary.")
        output_dict[value] = key   # returns values from origina dictionary in reverse order
    return output_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """This is a function to determine the most popular color in a dictionary."""
    most_popular_dict: dict[str, int] = {}  # initializing empty dictionary
    for key in color_dict:  # going through the keys of the input
        color = color_dict[key]
        if color in most_popular_dict: 
            most_popular_dict[color] += 1  # if color is already in the dictionary we will increase by one
        else:
            most_popular_dict[color] = 1  # If color is not in dictionary, we will add a key and corresponding value of one
        # finding the color that is the most popular
    most_pop_color = ''
    max_count = 0
    for color in most_popular_dict:
        count = most_popular_dict[color]
        if count > max_count:
            most_pop_color = color
            max_count = count
    return most_pop_color


def count(freq_list: list[str]) -> dict[str, int]:
    """Function to count the number of times a value appears."""
    counts_dict: dict[str, int] = {}  # Establishing an empty dictionary
    for item in freq_list:
        # use if statement to check if the item is already a key in the dictionary
        if item in counts_dict:
            counts_dict[item] += 1  # if item is in dictionary, it will increase by 1
        else:
            counts_dict[item] = 1  # if item is not in dictionary we will establish initial value of 1
    return counts_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Function that alphabetizes items based on their first letter."""
    alph_dict: dict[str, list[str]] = {}  # initializing empty dictionary that will include alphabetized words.
    # work through every word in the list
    for word in words: 
        first_letter = word[0].lower()  # use index to determine what the first letter of a word is and later add to dict ALSO convert to lowercase.
        if first_letter in alph_dict:  # Checking if letter is already in dict, if so, we will just add the word
            alph_dict[first_letter].append(word)
        else:  # If the letter is not already in the dictionary we will create a new key and associated value
            alph_dict[first_letter] = [word]
    return alph_dict


def update_attendance(exist_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Function to update attendance records for students."""
    if day in exist_dict:  # if the day is already in the dictionary, just add the student to the day
        if student not in exist_dict[day]:  # Ensuring the student is not already on the list for the day. 
            exist_dict[day].append(student)
        else: 
            print(f"{student} has already been marked as present for {day}.")
    else:  # if the day does not exist in the dictionary, create new key and value
        exist_dict[day] = [student]