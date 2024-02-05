"""EX_02 One Shot Battleship."""
__author__ = "730487065"
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2
GRID_SIZE: int = 4
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

correct: bool = False
while not correct:
    # Row input
    guess_row: str = input("Guess a row: ")
    guess = True
    while guess: 
        row_int: int = int(guess_row)
        if 1 <= row_int <= GRID_SIZE:
            guess = False
        else: 
            guess_row = input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ")
    # Column input
    guess_column: str = input("Guess a column: ")
    guess = True
    while guess:
        column_int: int = int(guess_column)
        if 1 <= column_int <= GRID_SIZE:
            guess = False
        else:
            guess_column = input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ")
    # Check if both row and column are correct
    if row_int == SECRET_ROW and column_int == SECRET_COLUMN:
        result_box = RED_BOX   # Red Box for correct guesses
    else:
        result_box = WHITE_BOX   # white box if guess is incorrect
    correct = True
# start counter
row_counter = 1
while row_counter <= GRID_SIZE:
    # initiating empty string 
    row_str = ""
    column_counter = 1
    if row_counter == row_int:
        while column_counter <= GRID_SIZE: 
            if column_counter == column_int:
                row_str += result_box
            else: 
                row_str += BLUE_BOX
            column_counter += 1
        row_counter += 1
    else:
        while column_counter <= GRID_SIZE: 
            row_str += BLUE_BOX
            column_counter += 1
        row_counter += 1
    print(row_str)

if row_int == SECRET_ROW and column_int == SECRET_COLUMN:
    print("Hit!")
elif row_int == SECRET_ROW and column_int != SECRET_COLUMN:
    print("Close! Correct row, wrong column.")
elif row_int != SECRET_COLUMN and column_int == SECRET_COLUMN:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")