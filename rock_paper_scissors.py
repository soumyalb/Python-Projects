# You want to create a simple game of Rock-Paper-Scissors in Python 
# that takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.

import random
options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)

user_choice = input("Enter Rock or Paper or Scissors: ")
if computer_choice == "Rock":
    if user_choice == "Rock":
        print(f"Draw: Play Again : Computer Choice is {computer_choice}")
    elif user_choice == "Paper":
        print(f"You win Paper beats Rock: Computer Choice is {computer_choice}")
    elif user_choice == "Scissors":
        print(f"You lose Rock beats Scissors: Computer Choice is {computer_choice}")
    else:
        print("Invalid")
elif computer_choice == "Paper":
    if user_choice == "Rock":
        print(f"You lose Paper beats Rock: Computer Choice is {computer_choice}")
    elif user_choice == "Paper":
        print(f"Draw: Play Again: Computer Choice is {computer_choice} ")
    elif user_choice == "Scissors":
        print(f"You win scissors beats paper: Computer Choice is {computer_choice}")
    else:
        print("Invalid")
elif computer_choice == "Scissors":
    if user_choice == "Rock":
        print(f"You win Rock beats Scissors: Computer Choice is {computer_choice}")
    elif user_choice == "Paper":
        print(f"You lose Scissors beats Paper: Computer Choice is {computer_choice}")
    elif user_choice == "Scissors":
        print(f"Draw: Play Again: Computer Choice is {computer_choice} ")
    else:
        print("Invlid")
