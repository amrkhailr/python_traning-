#9. Paint Job Estimator
#A painting company has determined that for every 115 square feet of wall space, one gallon of paint and eight hours of labor will be required. 
# The company charges $20.00 per hour for labor. Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. 
# The program should display the following data:
#• The number of gallons of paint required
#• The hours of labor required
#• The cost of the paint
#• The labor charges
#• The total cost of the paint job

def my_function(): 
    square_feet = float(input('What is the square feet of wall to be painted? '))
    Price_of_paint = input('What is the price of the paint per gallon? ')
    Number_of_paint_gallon_needed = (square_feet/115)*1
    Hours_needed = (square_feet/115)*8
    labor_charges = (Hours_needed/20)*1
    
    print('The number of gallons of paint required', Number_of_paint_gallon_needed )

my_function()





    




    

