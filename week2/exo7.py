# Sales Tax
# Write a program that will ask the user to enter the amount of a purchase. The program should then compute the state and county sales tax. Assume the state sales tax is 4 percent and the county sales tax is 2 percent. The program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).
# use the value 0.02 to represent 2 percent, and 0.04 to represent 4 percent.

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
