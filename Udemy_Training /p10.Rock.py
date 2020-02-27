import random

player_win = 0
computer_win = 0
winning_score = 3

while player_win < winning_score and computer_win < winning_score :
    print("player score: ", player_win, "computer score", computer_win)
    print("...rock...")
    print("...paper...")
    print("...scissors")

    player = input ("(Enter you choice): ").lower()
    if player == "quit" or player == "q":
        break
    random_num = random.randint(0, 2)
    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else: 
        computer = "scissors"

    print("The Computer plays", computer)

    if player == computer:
        print("its a tie")
    elif player == "rock":
        if computer == "paper":
            print("computer wins")
            computer_win += 1
        else:
            print("player wins")
            player_win += 1
    elif player == "paper":
        if computer == "rock":
            print("You win")
            player_win += 1
        else:
            print("Computer wins")
            computer_win += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer wins")
            computer_win += 1
        else:
            print("You win")
            player_win += 1
    else:
        print("please enter a valid move")
if player_win > computer_win:
    print(" You won")
else: 
    print("Computer won")
print("final scores... player: " ,player_win, "Computer..." ,computer_win)

        