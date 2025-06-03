import random

choices = ["rock", "paper", "scissors"]

emoji_map = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

class InvalidChoiceError(Exception):
    """Raised when the player inputs an invalid choice."""
    pass

def get_computer_choice():
    """Randomly select a choice for the computer."""
    return random.choice(choices)

def determine_winner(player, computer):
    """Determine the winner: 'player', 'computer' or 'draw'."""
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
