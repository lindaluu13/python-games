import random

choices = ["rock", "paper", "scissors"]

emoji_map = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

class InvalidChoiceError(Exception):
    pass

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "player"
    else: 
        return "computer"
