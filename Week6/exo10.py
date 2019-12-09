# Write code that does the following: opens an output file with the filename number_list.txt, 
# uses a loop to write the numbers 1 through 100 to the file, and then closes the file.

def main():
    infile = open('number_list.txt','w')
    for n in range(0,101):
        infile.write(str(n)+'\n')
    infile.close()
main()

