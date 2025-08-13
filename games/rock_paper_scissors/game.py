from .logic import get_computer_choice, get_user_choice, display_choices, determine_winner


def play():
    """Play Rock, Paper, Scissors"""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        computer_choice = get_computer_choice()

        user_choice = get_user_choice()

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        play_again = input("Play again ? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing! See you soon!")
            break
