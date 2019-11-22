#3. Budget Analysis
#Write a program that asks the user to enter the amount that he or she has budgeted for a
#month. A loop should then prompt the user to enter each of his or her expenses for the
#month, and keep a running total. When the loop finishes, the program should display the
#amount that the user is over or under budget.

budget = float(input("Enter your budget "))
x = "y"
y = 0
while x =='y':
    expenses = float(input('Enter Expense:')) 
    x = input('Enter y if you need to enter more expenses:')
    y = expenses + y
total = budget - y
print(total)
