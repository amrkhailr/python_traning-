#7. Odd/Even Counter In this chapter you saw an example of how to write an algorithm that determines 
#whether a number is even or odd. Write a program that generates 100 random numbers, 
#and keeps a count of how many of those random numbers are even and how many are odd. 

import random
def main():
    print("Odd/Even Counter")
    odd = 0
    even = 0
    print("Generating random numbers...")
    for count in range(100):
        num = random.randint(1,500)
        print(num)
    if check_even(num):
        even = even+1
    else:
        odd = odd +1
        print('Even numbers', even)
        print('Odd nummber', odd)
def check_even(num):
    if num % 2 == 0:
        print('True')
    else:
        print('False')
main()