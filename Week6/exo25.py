# 8. Random Number File Reader This exercise assumes you have completed Programming Exercise 7, Random Number File Writer. 
# Write another program that reads the random numbers from the file, display the numbers, and then display the following data: 
# • The total of the numbers • The number of random numbers read from the fil
def main():
    print('Random Number file reader')
    infile=open('random numbers writer.txt', 'r')
    total=0
    count=0
    for line in infile:
        num=int(line)
        print("Number: "+format(num,'.2f'))
        total+=num
        count+=1
    infile.close()
    print("toatl", total)
    print("Total", count)
main()
