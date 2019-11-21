#Celsius to Fahrenheit Table
#Write a program that displays a table of the Celsius temperatures 0 through 20 and their
#Fahrenheit equivalents. The formula for converting a temperature from Celsius to
#Fahrenheit is
#where F is the Fahrenheit temperature and C is the Celsius temperature. Your program
#must use a loop to display the table.

#F = 9
#5 C + 32

for n in range(20):
    f = ((9/5)*n)+32
    print('Celsius:', n, 'Fahrenheit:', f)

