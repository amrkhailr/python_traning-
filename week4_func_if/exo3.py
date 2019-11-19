#3. Mass and Weight
#Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the
#amount of mass of an object in kilograms, you can calculate its weight in newtons with the
#following formula:
#weight  mass  9.8
#Write a program that asks the user to enter an object’s mass, and then calculates its weight.
#If the object weighs more than 1,000 newtons, display a message indicating that it is too
#heavy. If the object weighs less than 10 newtons, display a message indicating that it is too
#light.

Mass = float(input("Please enter the object's mass: "))
Weight = Mass * 9.8

if Weight > 1000:
    print('It is too heavy!')
elif Weight < 10:
    print('It is too light!')
