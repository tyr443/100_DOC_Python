import random

import inquirer

options = ["rock", "paper", "scissors"]
win = 0
lose = 0
draw = 0
while True:
    opponent = random.choice(options)

    questions = [
        inquirer.List(
            'rps',
            message="Rock, paper or scissors?",
            choices=['Rock', 'Paper', 'Scissors', 'Exit'],
        ),
    ]

    answers = inquirer.prompt(questions)
    user_choice = answers["rps"].lower()

    if user_choice == "exit":
        print(f"Wins: {win}, Loses: {lose}, Draws: {draw}")
        exit()
    else:
        print(f"You chose: {user_choice} your opponent chose: {opponent}")
        if opponent == user_choice:
            print("It is a draw!")
            draw += 1
        elif opponent == "rock" and user_choice == "scissors":
            print("You Lose!")
            lose += 1
        elif opponent == "paper" and user_choice == "rock":
            print("You Lose!")
            lose += 1
        elif opponent == "scissors" and user_choice == "paper":
            print("You Lose!")
            lose += 1
        else:
            print("You Win!")
            win += 1
