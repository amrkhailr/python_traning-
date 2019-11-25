#2. Math Quiz Write a program that gives simple math quizzes. 
#The program should display two random numbers that are to be added, such as: 
#247 
#+ 129 
##The program should allow the student to enter the answer. 
#If the answer is correct, a message of congratulations should be displayed. 
#If the answer is incorrect, a message showing the correct answer should be displayed.

import random 

def main():
    print("Math Quiz")
    print("Enter the result of following number")
    num1 = random.randint(5,500)
    num2 = random.randint(100,900)
    print(" ",num1)
    print("+",num2)
    print("------")
    result = int(input(" "))
    if result == num1 + num2:
        print("Congertulation")
    else:
        print("Wrong answer")
main()
