import random
import time
from .utils import ask_guess, check_guess, MAX_ATTEMPTS

def play():
    fair_price = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    while attempts < MAX_ATTEMPTS:
        guess = ask_guess()
        attempts += 1
        if check_guess(guess, fair_price):
            break
        print(f"Attempts left: {MAX_ATTEMPTS - attempts}")
    
    end_time = time.time()
    duration = end_time - start_time

    if attempts == MAX_ATTEMPTS and guess != fair_price:
        print(f"Game over! The number was {fair_price}.")
    else:
        if duration < 60:
            print(f"You guessed it in {int(duration)} seconds.")
        else:
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            print(f"You guessed it in {minutes} min {seconds} sec.")