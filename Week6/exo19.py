#2. File Head Display: 
# Write a program that asks the user for the name of a file. 
# The program should display only the first five lines of the file’s contents. 
# If the file contains less than five lines, it should display the file’s entire contents.
def main():
    file1=open(input(str("please open")), 'r')
    line=file1.readline()
    count=0
    while line !='' and count <5:
        print(line)
        line=file1.readline()
        count = count+1
        file1.close
main()