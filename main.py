from games import number_guessing, rock_paper_scissors, hangman, word_guessing

def main():
    print("Choose a game:")
    print("1. Number Guessing")
    print("2. Rock, Paper, Scissor")
    print("3. Hangman")
    print("4. Word Guessing")

    choice = input("Enter your choice: ")

    if choice == '1':
        number_guessing.game.play()
    elif choice == '2':
        rock_paper_scissors.game.play()
    elif choice == '3':
        hangman.game.play()
    elif choice == '4':
        word_guessing.game.play()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
