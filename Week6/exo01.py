def main():
    #open the file apogee.txt
    infile = open('apogee.txt', 'r')
    #read the file content (if you put nothing then it will read everything, but i put 15 and it will only read 15 chracters now)
    file_content = infile.read(15)
    infile.close()
    #Print the output
    print(file_content)
main()