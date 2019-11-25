#For example, a salesperson with $16,000 in monthly sales will earn a 14 percent commission ($2,240). 
#Another salesperson with $18,000 in monthly sales will earn a 16 percent commission ($2,880). 
#A person with $30,000 in sales will earn an 18 percent commission ($5,400). 
#Because the staff gets paid once per month, 
#Hal allows each employee to take up to $2,000 per month in advance. 
#When sales commissions are calculated, 
#the amount of each employee’s advanced pay is subtracted from the commission. 
#If any salesperson’s commissions are less than the amount of their advance, 
#they must reimburse Hal for the difference. To calculate a salesperson’s monthly pay, 
#Hal uses the following formula: pay  sales  commission rate - advanced pay 
#Hal has asked you to write a program that makes this calculation for him. 
#he following general algorithm outlines the steps the program must take. 
#1.Get the salesperson’s monthly sales. 
#2. Get the amount of advanced pay. 
#3. Use the amount of monthly sales to determine the commission rate. 
#4. Calculate the salesperson’s pay using the formula previously shown. 
#If the amount is negative, indicate that the salesperson must reimburse the company.

def main():
    sales = get_sales ()
    advanced_pay = get_advanced_pay ()
    comm_rate = determine_comm_rate(sales)
    pay = sales * comm_rate - advanced_pay
    print('The pay is $', format(pay, ',.2f'), sep='')

    if pay < 0:
        print('The Salesperson must reimburse')
        print('the company.')
def get_sales():
    monthly_sales = float(input('Enter the monthly sales: '))
    return monthly_sales
def get_advanced_pay ():
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    advanced = float(input('Advanced pay: '))
    return advanced
def determine_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18
        return rate

main()



