#5. Color Mixer
#The colors red, blue, and yellow are known as the primary colors because they cannot be
#made by mixing other colors. When you mix two primary colors, you get a secondary color,
#as shown here:
#When you mix red and blue, you get purple.
#When you mix red and yellow, you get orange.
#When you mix blue and yellow, you get green.
#Design a program that prompts the user to enter the names of two primary colors to mix.
#If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. Otherwise, the program should display the name of the secondary
#color that results. 

primary = input('Enter the name of your first primary color to mix: ')
secondprimary = input('Enter the name of your second primary color to mix: ')


if primary == "red" and secondprimary == "blue":
    print('Your secondry color is purple')
elif primary == "red" and secondprimary == "yellow":
    print('Your secondry color is orange')
elif primary == "blue" or "yellow" and secondprimary == "yellow" or "blue": # A very creative way of Coding ROMAL!!!
    print('Your secondry color is green')
else:
    print('error')

