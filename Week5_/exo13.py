#1. Feet to Inches:
# One foot equals 12 inches. 
#Write a function named feet_to_inches that accepts a number of feet as an argument, 
#and returns the number of inches in that many feet. 
#Use the function in a program that prompts the user to enter a number of feet and then displays the 
#number of inches in that many feet. 

print('This program converts from feet to inches')
feet = int(input('Enter lenght in feet:'))

def feet_to_inches():
    print("Value in inches: ", feet*12)
feet_to_inches()