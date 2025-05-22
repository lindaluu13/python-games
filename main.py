from games import number_guessing, rock_paper_scissors

def main():
    print("Choose a game:")
    print("1. Number Guessing")
    print("2. Rock, Paper, Scissor")

    choice = input("Enter your choice: ")

    if choice == '1':
        number_guessing.game.play()
    elif choice == '2':
        rock_paper_scissors.game.play()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
