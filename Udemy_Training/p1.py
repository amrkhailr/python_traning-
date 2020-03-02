import random

player1 = input ("player1, make your move: ") .lower()


rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print("computer plays", computer)

if player1 == "rock" and computer == "scissors":
    print("player1 wins")
elif player1 == "rock" and computer == "paper":
    print("computer wins")
elif player1 == "paper" and computer == "rock":
    print("player1 wins")
elif player1 == "paper" and computer == "scissors":
    print("computer wins")
elif player1 == computer:
    print("its a tie")
else:
    print("something went wrong")