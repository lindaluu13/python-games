from .logic import get_computer_choice, determine_winner, InvalidChoiceError, choices, emoji_map

def play():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        try:
            computer = get_computer_choice()

            player = input("Choose rock, paper or scissors: ").lower()
            if player not in choices: 
                raise InvalidChoiceError(f"'{player}' is not a valid choice.")
            
            print(f"You chose: {player} {emoji_map[player]}")
            print(f"Computer chose: {computer} {emoji_map[computer]}")

            result = determine_winner(player, computer)

            if result == "draw":
                print("It's a draw")
            elif result == "computer":
                print("You lost :( Try again!")
            else:
                print("YOU WOOOON!!! Congrats!")

            play_again = input("Play again ? (y/n): ").lower()
            if play_again != 'y':
                print("Thanks for playing! See you soon!")
                break
            
        except InvalidChoiceError as e:
            print(f"Invalid input: {e}. Please choose rock, paper or scissors.")
