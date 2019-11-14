#11. Time Calculator 
# Write a program that asks the user to enter a number of seconds, and works as follows: 
#• There are 60 seconds in a minute. 
#If the number of seconds entered by the user is greater than or equal to 60, the program should display the number of minutes in that many seconds. 
#• There are 3,600 seconds in an hour. 
#If the number of seconds entered by the user is greater than or equal to 3,600, the program should display the number of hours in that many seconds. • 
#There are 86,400 seconds in a day. 
#If the number of seconds entered by the user is greater than or equal to 86,400, the program should display the number of days in that many seconds.

Time_calculator = int(input('Please enter the number of seconds: '))


Minutes = Time_calculator / 60
hour = Time_calculator / 3600
day = Time_calculator / 86400

if Time_calculator >= 86400:
    print('This is the number of day in that seconds',day)
elif Time_calculator >= 3600:
    print('This the number of hour in that seconds:',hour )
elif Time_calculator >= 60:
    print('This the number of minutes in that seconds:',Minutes )



