#6. Average of Numbers: 
# Assume that a file containing a series of integers is named numbers.txt 
# and exists on the computer’s disk. Write a program that calculates the average of all the numbers stored in the file.

def main():
    infile = open('sumofnumbers.txt', 'r')
    total =0
    count =0
    for line in infile:
        count+=1
        num = int(line)
        total+=num
    infile.close()
    print('The average number',total/count)
main()