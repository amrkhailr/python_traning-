#8. Stadium Seating
#There are three seating categories at a stadium. For a softball game, Class A seats cost $15, Class B seats cost $12, and Class C seats cost $9. 
# Write a program that asks how many tickets for each class of seats were sold, and then displays the amount of income generated from ticket sales.

def my_function():
    Class_A = 15
    Class_B = 12
    Class_C = 9

    Class_A_sold = float(input('How many Class A tickets were sold?'))
    Class_B_sold = float(input('How many Class B tickets were sold?'))
    Class_C_sold = float(input('How many Class C tickets were sold?'))

    Total_Class_A = Class_A_sold * Class_A
    Total_Class_B = Class_B_sold * Class_B
    Total_Class_C = Class_C_sold * Class_C
    Total = Total_Class_A + Total_Class_B + Total_Class_C
    
    print('Totall ticket sold: ', Total)
    

my_function()



