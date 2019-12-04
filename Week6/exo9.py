# Write a program that opens the my_name.txt file that was created by the program in question 1, reads your name from the file, 
# displays the name on the screen, and then closes the file.
def main():

    infile = open('myname.txt', 'r')
    file_content = infile.read()
    infile.close()
    print(file_content)
main()