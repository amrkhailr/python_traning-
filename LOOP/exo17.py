#8. Sum of Numbers
#Write a program with a loop that asks the user to enter a series of positive numbers. The
#user should enter a negative number to signal the end of the series. After all the positive
#numbers have been entered, the program should display their sum.

a = int(input("number:"))
total = 0
while a > 0:
    total = a + total
    a = int(input("number:"))
print(total)




