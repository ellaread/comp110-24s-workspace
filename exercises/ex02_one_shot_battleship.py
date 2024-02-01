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
    guess_row: str = input("Guess a row: ")
    row_int: int = int(guess_row)
    if row_int > GRID_SIZE or row_int < 1:
        row_int: int = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))
        # i think i need another conditional in here so this prompt keeps repeating until the value is in range
    if row_int != SECRET_ROW:
        print("Miss!")
    guess_column: str = input("Guess a column: ")
    column_int: int = int(guess_column)
    if column_int > GRID_SIZE or column_int < 1: 
        column_int: int = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: "))
    if column_int != SECRET_COLUMN:
        print("Miss!")
    correct = True
else:
    print("Hit!")