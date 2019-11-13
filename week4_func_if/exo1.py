 #Areas of Rectangles
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks
#for the length and width of two rectangles. The program should tell the user which rectangle
#has the greater area, or if the areas are the same.

widt1 = int(input('What is the Rectangles widt? '))
widt2 = int(input('What is the second Rectangles widt? '))
lenght1 = int(input('what is the Rectangles lenght? '))
lenght2 = int(input('what is the second Rectangles lenght? '))

Rectanglesarea1 = widt1 * lenght1
Rectanglesarea2 = widt2 * lenght2

if Rectanglesarea1 > Rectanglesarea2:
    print('Rectangle 1 area is greater than rectangle 2')
elif Rectanglesarea1 < Rectanglesarea2:
    print('Rectangle 1 area is smaller than rectangle 2 ')
else:
    print('Both Rectangles are the same')
