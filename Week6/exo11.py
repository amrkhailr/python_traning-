 #Write code that does the following: 
 # opens the number_list.txt file that was created by the code you wrote in question 3, 
 # reads all of the numbers from the file and displays them, and then closes the file.

def main():
    infile = open('number_list.txt', 'r')
    file_content = infile.read()
    infile.close()
    print(file_content)
main()