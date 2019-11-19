#10. Body Mass Index Program Enhancement
#In programming Exercise #6 in Chapter 3 you were asked to write a program that calculates a person’s body mass index (BMI). Recall from that exercise that the BMI is often used
#to determine whether a person is overweight or underweight for their height. A person’s
#BMI is calculated with the formula
#BMI  weight  703 / height2
#where weight is measured in pounds and height is measured in inches. Enhance the program so it displays a message indicating whether the person has optimal weight, is
#underweight, or is overweight. A person’s weight is considered to be optimal if his or
#her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered
#to be underweight. If the BMI value is greater than 25, the person is considered to be
#overweight.

weight = float(input('Please enter your weight '))
Height2 = float(input('Please enter your height '))

BMI = (weight * 703) / (Height2 * weight)

if BMI >= 18.5 and BMI <= 25:
    print('Your weight is considered to be optimal')
elif BMI < 18.5:
    print('You are considered underweight')
elif BMI > 25:
    print('You are considered overweight')