import random
from ..words import word_list

MAX_ATTEMPTS = 7

def get_random_word() -> str:
    """Return a random word from the list."""
    return random.choice(word_list).upper()

def ask_guess() -> str:
    """Ask the user for a letter or a word guess."""
    return input("🔤 Guess a letter or the full word: ").strip().upper()

def check_word(word: str, guess: str) -> bool:
    """Check if the guessed word matches the target."""
    return word == guess

def draw_hangman(attempts: int) -> None:
    """Display the hangman drawing based on number of incorrect attempts."""
    stages = [
        """
           -----
               |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[min(attempts, MAX_ATTEMPTS)])
