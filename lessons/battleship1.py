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
    while True: 
        row_int: int = int(guess_row)
        if 1 <= row_int <= GRID_SIZE:
            break
        else: 
            guess_row = input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ")
    # Column input
    guess_column: str = input("Guess a column: ")
    while True:
        column_int: int = int(guess_column)
        if 1 <= column_int <= GRID_SIZE:
            break
        else:
            guess_column = input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ")
    # Check if both row and column are correct
    if row_int == SECRET_ROW and column_int == SECRET_COLUMN:
        print("Hit!")
    else:
        print("Miss!")
    correct = True
