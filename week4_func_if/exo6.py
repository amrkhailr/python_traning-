#6. Change for a Dollar Game
#Create a change-counting game that gets the user to enter the number of coins required to make
#exactly one dollar. The program should prompt the user to enter the number of pennies,
#nickels, dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program should congratulate the user for winning the game. 
#Otherwise, the program should display a message indicating whether the amount entered was more than or less than one dollar.

pennie = 0.01
nickle = pennie * 5
dime = pennie * 10
quarter = pennie * 25

pennies = float(input('Enter the number of pennies '))
dimes = float(input('Enter the number of dimes '))
nickels = float(input('Enter the number of nickles '))
quarters = float(input('Enter the number of quarters '))

pennienumber = pennies * pennie
dimesnumber = dime * dimes
nickelsnumber = nickle * nickels
quarternumber = quarter * quarters

totall = pennienumber + dimesnumber + nickelsnumber + quarternumber

if totall == 1.00:
    print('Congertuations you WIN! :) ')
elif totall < 1.00:
    print("You didn't win one dollar :(")
else:
    print("You have more than one dollar. You didn't win game")


