import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

choices = [ROCK, PAPER, SCISSORS]

emoji_map = {
    ROCK: "🪨",
    PAPER: "📄",
    SCISSORS: "✂️"
}


class InvalidChoiceError(Exception):
    """Raised when the player inputs an invalid choice."""


def get_computer_choice():
    """Randomly select a choice for the computer."""
    return random.choice(choices)


def get_user_choice():
    """Ask the user a choice between r, p, s"""
    while True:
        try:
            user_choice = input("Choose rock, paper, or scissors (r/p/s): ")
            if user_choice in choices:
                return user_choice
            raise InvalidChoiceError(f"'{user_choice}' is not a valid choice.")
        except InvalidChoiceError as e:
            print(e)
            print('Try again')


def display_choices(user_choice, computer_choice):
    """Print the choices"""
    print(f"You chose: {emoji_map[user_choice]}")
    print(f"Computer chose: {emoji_map[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    """Determine the winner: 'user', 'computer' or 'draw'."""
    if user_choice == computer_choice:
        print("It's a draw")
    if (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("YOU WOOOON!!! Congrats!")
    print("You lost :( Try again!")
