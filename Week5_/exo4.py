#Dr. Kimura was so happy with the dice rolling simulator that you wrote for him, 
#he has asked you to write one more program. 
#He would like a program that he can use to simulate ten coin tosses, one after the other. 
#Each time the program simulates a coin toss, it should randomly display either “Heads” or “Tails”. 
#You decide that you can simulate the tossing of a coin by randomly generating a
#number in the range of 1 through 2. 
#You will write an if statement that displays “Heads” if the random number is 1, or “Tails” otherwise. 
#Here is the pseudocode: Repeat 10 times: 
#If a random number in the range of 1 through 2 equals 1 then: Display ‘Heads’ Else: 
#Display ‘Tails’ Because the program should simulate 10 tosses of a coin you decide to use a for loop. 
#The program is shown in Program

import random
HEADS = 1
TAILS = 2
TOSSES = 10
def main():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
        else:
            print('Tails')
main()