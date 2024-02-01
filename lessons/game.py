"""Number guessing game"""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while not correct: #correct == false
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    if guess > 10:
        print ("Too High!")
    if guess < 1:
        print ("Too Low!")
    else:
            print("Try again!")