#10. Golf Scores The Springfork Amateur Golf Club has a tournament every weekend. 
# The club president has asked you to write two programs: 
# 1. A program that will read each player’s name and golf score as keyboard input, 
# and then save these as records in a file named golf.txt. (Each record will have a field for the player’s name and a field for the player’s score.) 
# 2. A program that reads the records from the golf.txt file and displays them

def main():
    another='y'
    infile=open('golf.txt','a')
    while another == 'y' or another =='Y':
        print('Enter')
        name=input('Name')
        score=int(input('Score'))
        infile.write(name+'\n')
        infile.write(str(score)+'\n')
        print('Do you want add another')
        another=input('Y=yes, anything else=no')
        infile.close()
        print('Added to golf,txt')
main()
