"""EX03 - Functional Battle Ship."""

__author__ = "730475955"

import random


def input_guess(grid_size: int, RC: str) -> int:
    """User inputs a guess."""
    assert RC == "row" or RC == "column"
    if RC == "row":
        row_guess = int(input("Guess a row: "))
        while row_guess > grid_size:
            row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        while row_guess < 1:
            row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return row_guess
    if RC == "column":
        column_guess = int(input("Guess a column: "))
        while column_guess > grid_size:
            column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        while column_guess < 1:
            column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return column_guess
    return 0
    

def print_grid(grid_size: int, row_guess: int, column_guess: int, Correct: bool) -> None:
    """Prints Grid."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"

    if Correct is True:
        result: str = RED_BOX
    else:
        result = WHITE_BOX

    row_counter: int = 1

    while row_counter <= grid_size:
        row_string: str = str("")
        column_counter: int = int(1)
        if row_guess == row_counter:
            while column_counter <= grid_size:
                if column_guess == column_counter:
                    row_string += result
                else:
                    row_string += BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= grid_size:
                row_string += BLUE_BOX
                column_counter += 1
        print(row_string)
        row_counter += 1
    return None


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Determines if guess is correct."""
    if (secret_row == row_guess and secret_column == column_guess):
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main function of game."""
    turn_idx: int = 0
    Correct: bool = False
    while (turn_idx < 6 and Correct is False):
        print(f"=== Turn {turn_idx}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        Correct = correct_guess(secret_row, secret_column, row_guess, column_guess)
        grid: str = print_grid(grid_size, row_guess, column_guess, Correct)
        if Correct is True:
            print(grid)
            print("Hit!")
            print(f"You won in {turn_idx}/5 turns!")
            quit()
        else:
            print(grid)
            print("Miss!")
        turn_idx += 1
    if turn_idx == 6:
        print("X/5 - Better luck next time!")
        quit()
    return None


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))