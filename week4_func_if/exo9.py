#9. Shipping Charges
#The Fast Freight Shipping Company charges the following rates:
#Weight of Package Rate per Pound
#2 pounds or less $1.10
#Over 2 pounds but not more than 6 pounds $2.20
#Over 6 pounds but not more than 10 pounds $3.70
#Over 10 pounds $3.80
#Write a program that asks the user to enter the weight of a package and then displays the
#shipping charges.

Package_weight = int(input('Please enter the weight of your package in pound: '))

if Package_weight >= 2 and Package_weight <= 6:
    print('Your shipping charges will be $2.20')
elif Package_weight >= 6 and Package_weight <= 10:
    print('Your shipping charges will be $3.70')
elif Package_weight > 10:
    print('Your shipping charges will be $3.80')



