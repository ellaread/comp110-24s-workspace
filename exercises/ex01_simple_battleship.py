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

guess_str: str = ""

if guess_number == location_number:
    print("Correct! You hit the ship.")
    guess_str: str = RED_BOX

if guess_number != location_number:
    print("Incorrect! You missed the ship.")
    guess_str: str = WHITE_BOX

emoji_squares_str = "" # initializing an empty string
if guess_number == 1:
    emoji_squares_str = guess_str + BLUE_BOX * 3
    
if guess_number == 2:
    emoji_squares_str = BLUE_BOX + guess_str + BLUE_BOX*2

if guess_number == 3:
    emoji_squares_str = BLUE_BOX * 2 + guess_str + BLUE_BOX

if guess_number == 4:
    emoji_squares_str = BLUE_BOX*3 + guess_str
    
print(emoji_squares_str)


# if the guess is the first box, concatenate guess box, otherwise blue