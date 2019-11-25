#9. Prime Number List This exercise assumes you have already written the is_prime function 
#in Programming Exercise 8. Write another program that displays all of the prime numbers from 1 
#through 100. 
#he program should have a loop that calls the is_prime function. 

def main():
    print("Prime number list")
    print("Prime from 1 to 100")
    for count in range(2,101):
        if(is_prime(count)):
            print(count)

def is_prime(num):
    for count in range(2,num):
        if(num%count==0):
            print('True')
            print('False')
main()