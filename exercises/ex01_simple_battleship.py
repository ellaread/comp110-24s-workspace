"""EX01 - Simple Battleship - A cute step toward battles """

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
__author__ = "730487065"

pick_location: str = input("Pick a secret boat location between 1 and 4: ")
location_number: int = int(pick_location)
if location_number < 1:
    print(f"Error! {location_number} too low!")
if location_number > 4:
    print(f"Error! {location_number} too high!")

guess_location: str = input("Guess a number between 1 and 4: ")
guess_number: int = int(guess_location)
if guess_number < 1:
    print(f"Error! {guess_number} too low!")
if guess_number > 4:
    print(f"Error! {guess_number} too high!")

if guess_number == location_number:
    print("Correct! You hit the ship.")
    yes_str: str = RED_BOX
if guess_number != location_number:
    print("Incorrect! You missed the ship.")
    no_str: str = WHITE_BOX

emoji_squares_str = "" # initializing an empty string
if guess_number and location_number == 1:
    emoji_squares_str = yes_str + BLUE_BOX * 3
    print(emoji_squares_str)
else:
    emoji_squares_str = WHITE_BOX + BLUE_BOX * 3
    print(emoji_squares_str)


# if the guess is the first box, concatenate guess box, otherwise blue