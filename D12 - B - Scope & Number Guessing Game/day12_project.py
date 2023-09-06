import random
from art import logo

print(logo)

random_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
game_end = False

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

def attempt_reminder():
    print(f"\nYou have {attempts} attempts remaining to guess the number.")

while not game_end:
    attempt_reminder()
    guess = int(input("Make a guess: "))
    attempts -= 1
    difference = random_number - guess

    if difference == 0:
        print(f"You got it! The answer was {random_number}")
        game_end = True
    elif attempts == 0:
        print(f"You've run out of guesses, you lose. The answer was {random_number}")
        game_end = True
    elif difference > 0:
        print("Too low. \nGuess Again.")
    elif difference < 0:
        print("Too high. \nGuess Again.")