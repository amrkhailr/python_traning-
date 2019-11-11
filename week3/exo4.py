#2. Sale Tax Program Refactoring
#Programming Exercise 
#6 in Chapter 2 was the Sales Tax program. For that exercise you were asked to write a program that calculates and displays the county and state sales tax on a purchase. 
#If you have already written that program, redesign it so the subtasks are in functions. If you have not lready written that program, write it using functions.

def my_function():
    sst = 0.04
    cst = 0.02

    Amountofpurchase = float(input('what is your total amount of purchase ? '))
    salestaxcounty = cst *  Amountofpurchase
    salestaxstate = sst * Amountofpurchase
    totalsaletax = salestaxcounty + salestaxstate
    totalsaleplustax = Amountofpurchase + totalsaletax
    print('Your total purchase before TAX is' , Amountofpurchase )
    print('Your total county TAX is : ' , salestaxcounty)
    print('Your total state TAX  is : ' , salestaxstate)
    print('Your Tax is : ', totalsaletax )
    print('Your total sales plus tax is : ', totalsaleplustax )

my_function()