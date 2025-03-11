import random
import json

def get_user_choice():
    choices = ["✊", "✋", "✌️", "🦎", "🖖"]
    while True:
        try:
            user_input = int(input("Pick a number:\n1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖\n"))
            if user_input in [1, 2, 3, 4, 5]:
                return choices[user_input - 1]
            else:
                print("Invalid input. Please pick a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    choices = ["✊", "✋", "✌️", "🦎", "🖖"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    rules = {
        "✊": ["✌️", "🦎"],
        "✋": ["✊", "🖖"],
        "✌️": ["✋", "🦎"],
        "🦎": ["🖖", "✋"],
        "🖖": ["✊", "✌️"]
    }
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in rules[user_choice]:
        return "The player won!"
    else:
        return "The computer won!"

def play_round(player_name, player_score, computer_score):
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\n{player_name} chose: {user_choice}")
    print(f"CPU chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    if result == "The player won!":
        player_score += 1
    elif result == "The computer won!":
        computer_score += 1
    return player_score, computer_score, result

def play_game():
    print("================================\nRock Paper Scissors Lizard Spock\n================================")
    player_name = input("Enter your name: ")
    rounds = int(input("How many rounds do you want to play? "))
    player_score = 0
    computer_score = 0
    game_history = []

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}:")
        player_score, computer_score, result = play_round(player_name, player_score, computer_score)
        game_history.append({"round": round_number, "player_choice": player_name, "computer_choice": get_computer_choice, "result": result})
        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

    print("\nGame Summary:")
    for entry in game_history:
        print(f"Round {entry['round']}: {entry['player_choice']} chose {entry['player_choice']}, CPU chose {entry['computer_choice']} - {entry['result']}")

    if player_score > computer_score:
        print(f"\n{player_name} won the game!")
    elif computer_score > player_score:
        print("\nThe computer won the game!")
    else:
        print("\nThe game is a tie!")

def main():
    play_game()

if __name__ == "__main__":
    main()