#The while Loop: a Condition-Controlled Loop:

1 # This program calculates sales commissions.
def main():
    keep_going = 'y'
    while keep_going == 'y': # Keep going on until user enter y and stop if user enters any other word,
        sales = float(input('Enter the amount of sales: '))
        comm_rate = float(input('Enter the commission rate: '))
        commission = sales * comm_rate
        print('The commission is $', \
              format(commission, ',.2f'), sep='')
        keep_going = input('Do you want to calculate another ' + \
                           'commission (Enter y for yes): ')

main()
#############################################################################

MAX_TEMP = 102.5

def main():
    
    temperature = float(input("Enter the substance's Celsius temperature: "))
    while temperature > MAX_TEMP:
        
        print('The temperature is too high.')
        print('Turn the thermostat down and wait')
        print('5 minutes. Then take the temperature')
        print('again and enter it.')
        temperature = float(input('Enter the new Celsius temperature: '))
    print('The temperature is acceptable.')
    print('Check it again in 15 minutes.')
main()