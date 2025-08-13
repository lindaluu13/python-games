from .utils import get_random_word, ask_guess, check_word, draw_hangman, MAX_ATTEMPTS


def play():
    """Play the Hangman"""
    print("🎮 Welcome to Hangman!")

    word_to_guess = get_random_word()
    hidden_word = ["_"] * len(word_to_guess)
    attempts = 0
    guessed_letters = set()
    guessed_words = set()

    print(
        f"\n🔠 The word to guess contains {len(word_to_guess)} letters: {' '.join(hidden_word)}")

    while attempts < MAX_ATTEMPTS:
        guess = ask_guess()

        if not guess.isalpha():
            print("❗ Invalid input. Use only letters.")
            continue

        # Full word guess
        if len(guess) > 1:
            if guess in guessed_words:
                print("⚠️ You've already tried this word!")
                continue

            guessed_words.add(guess)

            if check_word(word_to_guess, guess):
                print(f"\n🎉 Congrats! You found the word: {word_to_guess}")
                return
            attempts += 1
            print("❌ Wrong word! You lost 1 life.")
            draw_hangman(attempts)

        # Single letter guess
        else:
            if guess in guessed_letters:
                print("⚠️ You've already tried this letter!")
                continue

            guessed_letters.add(guess)

            if guess in word_to_guess:
                print("✅ Correct letter!")
                for i, letter in enumerate(word_to_guess):
                    if letter == guess:
                        hidden_word[i] = guess
            else:
                attempts += 1
                print("❌ Wrong letter! You lost 1 life.")
                draw_hangman(attempts)

        # Display progress
        print(f"\n🟦 Word: {' '.join(hidden_word)}")
        print(f"❤️ Remaining lives: {MAX_ATTEMPTS - attempts}")

        # Win condition
        if "_" not in hidden_word:
            print(f"\n🏆 Congrats! You found the word: {word_to_guess}")
            return

    print(f"\n💀 Game over! The word was: {word_to_guess}")
