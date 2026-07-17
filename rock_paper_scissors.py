import random 
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'


emojis = {
    ROCK: '✊',  # Rock
    PAPER: '✋',  # Paper
    SCISSORS: '✌️'   # Scissors
}
choices = tuple(emojis.keys())

def get_user_choice(player_name):
    while True:
        user_choice = input(f"{player_name}, choose Rock, Paper, or Scissors (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.")


def display_choices(player1_choice, player2_choice):
    print(f"Player 1 chose: {emojis[player1_choice]}")
    print(f"Player 2 chose: {emojis[player2_choice]}")

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (
        (player1_choice == ROCK and player2_choice == SCISSORS) or
        (player1_choice == PAPER and player2_choice == ROCK) or
        (player1_choice == SCISSORS and player2_choice == PAPER)
    ):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game():
    player_count = 0
    player1_count = 0
    player2_count = 0
    ties_count =0
    while True:
        player1_choice = get_user_choice("Player 1")
        player2_choice = get_user_choice("Player 2")

        display_choices(player1_choice, player2_choice)
        result = determine_winner(player1_choice, player2_choice)
        print(result)
        player_count += 1

        if result == "Player 1 wins!":
            player1_count += 1
        elif result == "Player 2 wins!":
            player2_count += 1
        else:
            ties_count += 1

        should_continue = input("Do you want to play again? (yes/no): ").lower()
        if should_continue == "no":
            print(f"You played {player_count} rounds.")
            print(f"Player 1 wins: {player1_count}, Player 2 wins: {player2_count}, Ties: {ties_count}")
            break

play_game()
