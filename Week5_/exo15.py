#3. Maximum of Two Values Write a function named maximum that accepts two integer values as arguments 
# and returns the value that is the greater of the two. 
# For example, if 7 and 12 are passed as arguments to the function, the function should return 12. 
# Use the function in a program that prompts the user to enter two integer values. 
# The program should display the value that is the greater of the two

def main():
    print("Enter two maximum values")
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    if num1 > num2:
        print(num1)
    elif num1 == num2:
        print("Both values are equal")
    else:
        print(num2)
main()