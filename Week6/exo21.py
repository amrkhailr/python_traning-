#4. Item Counter:
#  Assume that a file containing a series of names (as strings) is named names.txt and exists on the computer’s disk. 
# Write a program that displays the number of names that are stored in the file. 
# (Hint: Open the file and read every string stored in it. Use a variable to keep a count of the number of items that are read from the file.)

def main():
    print("Item Counter")
    infile = open('My_names.txt', 'r')
    count=0
    for line in infile:
        count+=1
        print(line.rstrip('\n'))
    print("Total names: ", count)
    infile.close()
    input()
main()