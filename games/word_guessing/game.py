from .utils import get_random_word, ask_guess


def play():
    """Play Word Guessing"""
    word_to_guess = get_random_word()
    hidden_word = ["_"] * len(word_to_guess)
    guessed_letters = set()

    print("🎮 Welcome to Word Guessing!")
    print(f"🧠 The word has {len(word_to_guess)} letters.")

    while "_" in hidden_word:
        print("\nWord to guess:", " ".join(hidden_word))
        user_guess = ask_guess()

        if user_guess in guessed_letters:
            print("⚠️ You've already tried this letter!")
            continue

        guessed_letters.add(user_guess)

        if user_guess in word_to_guess:
            print("✅ Well done!")
            for i, letter in enumerate(word_to_guess):
                if letter == user_guess:
                    hidden_word[i] = user_guess
        else:
            print("❌ WRONG! This letter isn't in the word!")

    print("\n🎉 Congrats! You guessed the word:", word_to_guess)
