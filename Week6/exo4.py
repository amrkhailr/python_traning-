def main():
    #open the file apogee.txt
    infile = open('apogee.txt', 'r')
    #read the file content (if you put nothing then it will read everything, but i put 15 and it will only read 15 chracters now)
    file_content = infile.read()
    infile.close()
    # split will create a list of all the content in the vairable saved
    file_content = file_content.splitlines()

    # will create a loop with characters number lenght
    for n in file_content:
        print(n+ ' : ' + str(len(n)))
main()