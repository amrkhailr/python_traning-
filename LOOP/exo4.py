#Write a loop that asks the user to enter a number. The loop should iterate 10 times and
#keep a running total of the numbers entered.

expenses=10
month=0.0 

for sum in range(expenses):
    amount=float(input('Enter monthly expense amount: '))
    month=month + amount
print('Your TOTAL EXPENSE AMOUNT is:$',month,)
    