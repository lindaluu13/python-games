import random
from ..words import word_list


def get_random_word() -> str:
    """Return a random word from the list."""
    return random.choice(word_list).upper()


def ask_guess() -> str:
    """Ask the user for a single letter guess."""
    while True:
        guess = input("🔤 Guess a letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("⛔ Please enter only ONE valid letter.")
        else:
            return guess
