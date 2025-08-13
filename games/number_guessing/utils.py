MAX_ATTEMPTS = 7


def ask_guess():
    """Ask the user for a number between 1 and 100."""
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            if guess <= 0 or guess > 100:
                print("Number must be between 1 and 100.")
            else:
                return guess
        except ValueError:
            print("Invalid input. Try again.")


def check_guess(guess, number_to_guess):
    """Compare guess with the correct number and give feedback."""
    if guess > number_to_guess:
        print("Too high!")
        return False
    elif guess < number_to_guess:
        print("Too low!")
        return False
    else:
        print("THE NUMBER IS CORRECT! YOU WOOOOON!!!")
        return True
