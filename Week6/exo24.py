#7. Random Number File Writer Write:
# a program that writes a series of random numbers to a file. 
# Each random number should be in the range of 1 through 100. 
# The application should let the user specify how many random numbers the file will hold.

import random
def main():
    count = input("Enter a number")
    infile = open('output.txt','w')
    while count !=0:
        num = random.randint(1,100)
        infile.write(str(num)+'')
        count+=1
        infile.close()
        print("numbers stored in the file")
main()
