#Write a while loop that asks the user to enter two numbers. The numbers should be
#added and the sum displayed. The loop should ask the user if he or she wishes to perform the operation again. 
#If so, the loop should repeat, otherwise it should terminate.

num = 1
num2 = 'y'


while num2 == 'y':
    number1 = int(input('Please enter your first number: '))
    number2 = int(input('Please enter your second number: '))
    total = number1 + number2
    print('Your total sum for',total )
    num2(input('Would you like to enter another numbers? for yes enter y'))

