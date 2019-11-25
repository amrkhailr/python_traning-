#You will write a while loop that simulates one roll of the dice, 
#and then asks the user if another roll should be performed.
#As long as the user answers “y” for yes, the loop will repeat
import random 
 # frist import all the ransom functions
  #Constants for the minimum and maximum random numbers
MIN = 1
MAX = 6 
def main():
    again = 'y' ## Create a variable to control the loop.
    while again == 'y' or again == 'Y': #Simulate rolling the dice.
        print('Rolling the dice...')
        print('Their values are :')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        # Do another roll of the dice?
        again = input('Roll them again? (y = yes):')
main()



