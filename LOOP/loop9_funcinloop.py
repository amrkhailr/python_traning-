#This program calculates sales commissions.
def main():
    keep_going = 'y'
    while keep_going == 'y':

        show_commission()
        keep_going = input('Do you want to calculate another ' + \
        'commission (Enter y for yes): ')

# we can do the same calculation with function alone as follwoing.

def show_commission():

    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    commission = sales * comm_rate

    print('The commission is $', \
    format(commission, ',.2f'), sep='')

main()