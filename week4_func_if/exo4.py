 #Magic Dates The date June 10, 1960, is special because when it is written in the following format, 
 #the month times the day equals the year: 6/10/60 Design a program that asks the user to enter a month (in numeric form), a day, and a twodigit year. 
 #The program should then determine whether the month times the day equals the year. 
 #If so, it  should display a message saying the date is magic. Otherwise, it should display a message saying the date is not magic.

Month = int(input('Please enter your month: '))
Date = int(input('Please enter your date: '))
Year = int(input('Please enter your year: '))

month_day = Month * Date


if month_day == Year:
    print('The date is Magic')
else:
    print('The date is not Magic')



    