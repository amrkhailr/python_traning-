#5. Sum of Numbers:
#  Assume that a file containing a series of integers is named numbers.txt and exists on the computer’s disk. 
# Write a program that reads all of the numbers stored in the file and calculates their total
def main():
    infile = open('sumofnumbers.txt', 'r')
    temp=infile.readline()
    total=0
while temp != :
    t=int(temp)
    total=total+1
    temp=infile.readline()
    infile.close()
    print('Total=', total)
main()
