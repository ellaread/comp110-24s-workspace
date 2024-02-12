"""Functional Battleship Game!"""
__author__: 730487065
import random 
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# coming up with function for user to input guesses and to reprompt for guesses out of range
def input_guess(grid_size: int, specification: str) -> int:
    assert specification == "row" or specification == "column"
    if specification == "row": 
        guessr = int(input("Guess a row: "))
        while guessr < 1 or guessr > grid_size: 
            guessr = int(input (f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return guessr
    if specification == "column":
        guessc = int(input("Guess a column:"))
        while guessc < 1 or guessc > grid_size: 
            guessc = int(input (f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return guessc
#function to print battleship grid and have different colors depending on it guess is correct
def print_grid(grid_size, guessr, guessc, correct: bool):
    row_counter = 1
    while row_counter <= grid_size:
        if correct:
            result_box = RED_BOX   # red box for correct guesses
        else:
            result_box = WHITE_BOX   # white box if guess is incorrect
        row_str = ""  # initiating empty string 
        column_counter = 1 # start column counter
        while column_counter <= grid_size: 
            if column_counter == guessc and row_counter == guessr:
                row_str += result_box
            else: 
                row_str += BLUE_BOX
            
            column_counter += 1
        print(row_str)
        row_counter += 1
#function to determine if guessed location = secret location -- T/F
def correct_guess(secretr: int, secretc: int, guessr, guessc) -> bool:
   return secretr == guessr and secretc == guessc
#main function that compiles all the previous functions to streamline the game
def main(grid_size, secretr, secretc):
    turns = 5 # defined so that the game will stop after 5 turns and not continue forever
    current_turn = 1
    win = False
    while turns > 0 and not win:
        print(f"=== Turn {current_turn}/5 ===")
        guessr = input_guess(grid_size, "row")
        guessc = input_guess(grid_size, "column")
        correct = correct_guess(secretr, secretc, guessr, guessc)
        print_grid(grid_size, guessr, guessc, correct)
        if correct:
            print(f"Hit! You won in {current_turn}/5 turns!")
            win = True
        else:   # do not print anything about correct guesses this time 
            print("Miss!")
            current_turn += 1
            turns -= 1
    if not win:   # if location is not correctly guessed in 5 moves print this 
        print("X/5 - Better luck next time!")
if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
