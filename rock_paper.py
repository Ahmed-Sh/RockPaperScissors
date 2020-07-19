import random

user_name = input("Enter your name: ")
score = 0
print(f"Hello, {user_name}")
with open("rating.txt", "r") as f:
    for lines in f:
        data = lines.split()
        if data[0] == user_name:
            score = data[1]

starting_option = input()

if starting_option == "":
    odds = ["rock", "paper", "scissors"]
else:
    odds = starting_option.split(",")

print("Okay, let's start")
while True:
    player_input = input()
    if player_input in odds:
        computer_choice = random.choice(odds)
        new_list = odds[odds.index(computer_choice) + 1:] + odds[:odds.index(computer_choice)]
        if player_input == computer_choice:
            print(f"There is a draw {player_input}")
            score += 50
        elif player_input in new_list[:int(len(new_list) / 2)]:
            print(f"Well done. Computer chose {computer_choice} and failed ")
            score += 100
        else:
            print(f"Sorry, but computer chose {computer_choice}")

    elif player_input == "!exit":
        print("Bye!")
        break

    elif player_input == "!rating":
        print(f"Your rating: {score}")
    else:
        print("Invalid input")
