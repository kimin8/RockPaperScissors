import random

computer_wins = 0
player_wins = 0

print('Choose one of the following: rock, paper or scissors... You can type "quit" to exit')
player_input = input()

while player_input != "quit":
    computer_choice = random.choice(("rock", "paper","scissors"))

    if player_input != "rock" and player_input != "paper" and player_input != "scissors" and player_input != "quit":
        raise SystemExit("Invalid input! The game crashed! Please restart...")

    if player_input == "rock" and computer_choice == "scissors" \
        or player_input == "paper" and computer_choice == "rock" \
        or player_input == "scissors" and computer_choice == "paper":
        print(f"The computer chose {computer_choice}.")
        player_wins += 1
        print("\033[92m{}\033[00m".format("You win!"))
        print(f"You {player_wins} : {computer_wins} Computer")

    elif player_input == "rock" and computer_choice == "rock" \
        or player_input == "paper" and computer_choice == "paper" \
        or player_input == "scissors" and computer_choice == "scissors":
        print(f"The computer chose {computer_choice}.")
        print("\033[96m{}\033[00m".format("Draw!"))
        print(f"You {player_wins} : {computer_wins} Computer")
    else:
        print(f"The computer chose {computer_choice}.")
        computer_wins += 1
        print("\033[91m{}\033[00m".format("You lose!"))
        print(f"You {player_wins} : {computer_wins} Computer")

    print('Choose one of the following: rock, paper or scissors... You can type "quit" to exit')
    player_input = input()

print("Thank you for playing!")