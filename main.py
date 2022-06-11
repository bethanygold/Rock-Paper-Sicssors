import random

print("Welcome to the game of Rock, Paper, Sicssors")

while True:
    choices = ['R', 'P', 'S']

    computer = random.choice(choices)
    player = input("Pick an option ['R', 'P', 'S']: ").upper()

    while player not in choices:
        print("Invalid input, use any of the following: ['R', 'P', 'S']")
        player = input("Pick an option ['R', 'P', 'S']: ").upper()

    if player == computer:
        print("CPU: ", computer)
        print("Player: ", player)
        print("Tie!")
    elif player == "R":
        if computer =="P":
            print("CPU: ", computer)
            print("Player: ", player)
            print("Computer wins!")
        if computer =="S":
                print("CPU: ", computer)
                print("Player: ", player)
                print("Player wins!")
        break
    elif player == "S":
        if computer =="R":
            print("CPU: ", computer)
            print("Player: ", player)
            print("Computer wins!")
        if computer =="P":
                print("CPU: ", computer)
                print("Player: ", player)
                print("Player wins!")
        break
    elif player == "P":
        if computer =="S":
            print("CPU: ", computer)
            print("Player: ", player)
            print("Computer wins!")
        if computer =="R":
                print("CPU: ", computer)
                print("Player: ", player)
                print("Player wins!")
        break
   

print("Thanks for playing, bye!")