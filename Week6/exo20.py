#3. Line Numbers Write a program that asks the user for the name of a file. 
# The program should display the contents of the file with each line preceded with a line number followed by a colon. 
# The line numbering should start at 1

def main():
    print("Line numbers")
    fname = input("Enter File name: ")
    infile = open(fname,'r')
    count = 0
    for line in infile:
        count+=1
        print(count,".",line.strip('\n'))
    infile.close()
    input()
main()





OROOOOOOOOOOOOOoRRRRRRRRRRRRRRR


fn = input("gice a file name")
with open (fn, "r") as f:
    c= f.read()
    c=c.splitlines()
    k=c[:5]
    for i in k:
        print(i)