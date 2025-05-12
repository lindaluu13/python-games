from games import number_guessing

def main():
    print("Choose a game:")
    print("1. Number Guessing")
    choice = input("Enter your choice: ")

    if choice == '1':
        number_guessing.game.play()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
