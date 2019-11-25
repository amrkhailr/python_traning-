#11. Random Number Guessing Game Write a program that generates a random number in the range of 1 
#through 100 and asks the user to guess what the number is. 
#If the user’s guess is higher than the random number, the program should display “Too high, 
#try again.” If the user’s guess is lower than the random number, 
#the program should display “Too low, try again.
#” If the user guesses the number, the application should congratulate the user and 
# generate a new random number so the game can start over. 
# Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the user makes. 
# When the user correctly guesses the random number, 
#the program should display the number of guesses

import random

while True:
    found = False
    counter = 0
    number = random.randint(0,10)
    print("random number generated")
while not found:
    guess = int(input("Guess the number "))
    count+=1
    if guess == number:
        print("right")
        found = True
        print()
    elif  guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
