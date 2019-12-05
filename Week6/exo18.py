#1. File Display: 
# Assume that a file containing a series of integers is named numbers.txt and exists on the computer’s disk. 
# Write a program that displays all of the numbers in the file.
def main():
    infile = open('numberss.txt', 'r')
    for line in infile:
        number=int(line)
    print(number)
    infile.close
main()