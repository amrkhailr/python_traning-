#7. Pennies for Pay
#Write a program that calculates the amount of money a person would earn over a period
#of time if his or her salary is one penny the first day, two pennies the second day, and
#continues to double each day. The program should ask the user for the number of days.
#Display a table showing what the salary was for each day, and then show the total pay at
#the end of the period. The output should be displayed in a dollar amount, not the number
#of pennies

n = 0 
days = int(input('Number of days you have worked'))
for n in range(days+1):
    salary = n * 2
    dollar = salary/100
    print('$'+str(dollar))
print('Total Salary: $'+str(dollar))



