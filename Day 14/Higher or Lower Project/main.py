import random
import art  # This is assumed to contain 'logo' and 'vs' ASCII art
from game_data import data  # This contains the list of celebrity/influencer data


def get_random_account(exclude=None):
    account = random.choice(data)
    while account == exclude:
        account = random.choice(data)
    return account


def format_account(account, label):
    return f"{label}: {account['name']}, a {account['description']}, from {account['country']}."


def check_answer(choice, a, b):
    if choice == 'a':
        if a['follower_count'] > b['follower_count']:
            return True, a  # Keep A
    elif choice == 'b':
        if b['follower_count'] > a['follower_count']:
            return True, b  # B becomes new A
    return False, a  # Wrong answer, game ends


def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    a = get_random_account()

    while game_should_continue:
        b = get_random_account(exclude=a)

        print(format_account(a, "Compare A"))
        print(art.vs)
        print(format_account(b, "Against B"))

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choice not in ['a', 'b']:
            print("Invalid input. Please type 'A' or 'B'.")
            continue

        is_correct, new_a = check_answer(choice, a, b)

        if is_correct:
            score += 1
            a = new_a  # Move forward
            print(f"\nYou're right! Current score: {score}.\n")
        else:
            game_should_continue = False
            score = 0
            print(f"\nSorry, that's wrong. Final score: {score}")


# Start the game
game()
