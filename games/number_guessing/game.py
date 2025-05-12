import random
from .utils import ask_guess, check_guess, MAX_ATTEMPTS

def play():
    fair_price = random.randint(1, 100)
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        guess = ask_guess()
        attempts += 1
        if check_guess(guess, fair_price):
            break
        print(f"Attempts left: {MAX_ATTEMPTS - attempts}")

    if attempts == MAX_ATTEMPTS:
        print(f"Game over! The number was {fair_price}.")