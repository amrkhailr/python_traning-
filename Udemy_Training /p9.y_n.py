import random 

my_number = random.randint(1,10)

guess = None

while True:
    guess = int(input("pick a number 1 to 10: "))
    if guess < my_number:
        print("Too Low")
    elif guess > my_number:
        print("Too much")
    else:
        print("You won")
        play_again = input("Do you wanna play again? (y/n")
        if play_again == "y":

            my_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing")
            break