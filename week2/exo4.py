Percentage = 0.23
Projectedamount=float(input("What is your projected amount of sales :"))
profit = Projectedamount * Percentage
print('Your Profit is: ', profit)

Acre = 43560
Totaltrack=int(input("What is your total squar feet : "))
Calculatedamountofacres= Acre / Totaltrack
print('Your TatalSquarFeet will be',Calculatedamountofacres)

item1 = float(input('Item1 price'))
item2 = float(input('item2 price'))
item3 = float(input('item3 proce'))
item4 = float(input('item4 price'))
item5 = float(input('item5 price'))
totaleitems = item1 + item2 + item3 + item4 + item5
taxsales = totalitems  * 0.06
subtotal = totalitems + taxsales 

print('Total item prices with no TAX', totalitems)
print('')