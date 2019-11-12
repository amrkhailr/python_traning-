#Body Mass Index
#Write a program that calculates and displays a person’s body mass index (BMI). The BMI is often used to determine whether a person is overweight or underweight for his or her height. 
# A person’s BMI is calculated with the following formula: 
#BMI  = weight x 703 / height2
def my_function():

    weight = float(input('Please type your weight in pound'))
    height2 = float(input('Please type your height in inches'))
    BMI  = weight * (703 / height2)
    print('Your body mass is ',BMI)

my_function()



