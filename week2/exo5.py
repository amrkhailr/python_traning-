item1 = int(input('Item1 price'))
item2 = int(input('item2 price'))
item3 = int(input('item3 price'))
item4 = int(input('item4 price'))
item5 = int(input('item5 price'))
totalitems = item1 + item2 + item3 + item4 + item5
taxsales = totalitems  * 0.06
subtotal = totalitems + taxsales 

print('Total item prices with no TAX', totalitems)
print('Total Tax price for all the Items', taxsales)
print('Subtotal item prices including TAX', subtotal)