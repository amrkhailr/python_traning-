#5. Property Tax
#A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. 
# For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then 64￠ for each $100 of the assessment value. 
# The tax for the acre assessed at $6,000 will be $38.40. Write a program that asks for the actual value of a piece of roperty and displays the assessment value and property tax.

def my_function():

    propertymarketprice = float(input('What is your property market value? '))

    assessment_value = propertymarketprice * 0.6
    tax_price = assessment_value * 0.64

    print('Your property assessment value is',assessment_value,'$')
    print('Your assessment value TAX amount is',tax_price,'$')

my_function()







