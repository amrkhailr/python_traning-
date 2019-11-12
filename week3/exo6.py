#Automobile Costs
#Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: 
#loan payment, insurance, gas, oil, tires, and maintenance. The program should then display the total monthly cost of these expenses, and the total annual cost of hese expenses

def my_function():
    Loan = float(input('How much you spend on Loan? '))
    insurance = float(input('How much you spend on insurance? '))
    Gas = float(input('How much you spend on Gas? '))
    Oil = float(input('How much you spend on Oil? '))
    Tires = float(input('How much you spend on Tires? '))
    maintenance = float(input('How much you spend on Maintenince? '))
    monthlyspends = Loan + insurance + Gas + Oil + Tires + maintenance
    annualspends = monthlyspends * 12
    print('Your total monthly expence is ', monthlyspends)
    print('Your total annual expence is ', annualspends )

my_function()



