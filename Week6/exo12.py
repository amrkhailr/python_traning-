# Modify the code that you wrote in question 4 so it adds 
# all of the numbers read from the file and displays their total.
def main():
     
    infile = open('number_list.txt', 'r')
    temp = infile.readline()
    sum=0
    while temp != sum :
        t=int(input(temp))
        sum=sum+t
        temp=infile.readline()
    infile.close()
    print('Sum=',sum)
main()
