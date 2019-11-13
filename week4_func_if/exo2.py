#1. Roman Numerals
#Write a program that prompts the user to enter a number within the range of 1 through 10.
#The program should display the Roman numeral version of that number. If the number is
#outside the range of 1 through 10, the program should display an error message. The following table shows the Roman numerals for the numbers 1 through 10:


number = float(input('Print your number in between 1 -10 : '))
if  number >= 1 and number <= 10:
    if number == 1:
        print('Your Roman number is I')
    if number == 2:
        print('Your Roman number is II')
    if number == 3:
        print('Your Roman number is III')
    if number == 4:
        print('Your Roman number is IV')
    print('Your number is in between 1 and 10')
else:
    print('Your number is out the range')
