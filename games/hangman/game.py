from .words import word_list
import random

def play():
    print("Welcome to Hangman!")

    tries = 1
    word = random.choice(word_list).upper()
    guess = "_" * len(word)
    print(word)
    print(guess)
    guessed_words = []
    guessed_letters = []

    while tries > 0 and guess != word:   
        g = input("Guess a letter or a word: ").upper()
        guessed_words.append(g)
        guessed_letters.append(g)
        if tries == 7:
            break
        
