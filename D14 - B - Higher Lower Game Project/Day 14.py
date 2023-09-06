from random import *
from art import *
from gamedata import *


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, from {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    """Use if statement to check if user is correct."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = choice(data)

# Make game repeatable
while game_should_continue:
    # Generate a random account from the game data.
    account_a = account_b
    account_b = choice(data)

    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    if is_correct:
        # Score keeping.
        score += 1
        print(f"You're right. Current score: {score}")
    else:
        game_should_continue = False
        print(f"That's wrong. Final score: {score}")


# Clear the screen between rounds
