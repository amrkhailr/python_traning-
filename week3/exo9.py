#7. Calories from Fat and Carbohydrates
#A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, 
# she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. 
# Then, she calculates the number of calories that result from the fat, using the following formula:
#calories from fat =fat grams x 9
#Next, she calculates the number of calories that result from the carbohydrates, using the
#following formula:
#calories from carbs = carb grams x 4
#The nutritionist asks you to write a program that will make these calculations.

def my_function():
    Consumed_fat = float(input('How much fat grams did you consumed in a day? '))
    Consumed_carbohydrate = float(input('How much carbohydrate grams did you consumed in a day? '))
    Calories_from_fat = Consumed_fat * 9
    Calories_from_carbohydrate = Consumed_carbohydrate*4

    print('Number of calories that result from the fat ',Calories_from_fat)
    print('Number of calories that result from the carbohydrate ',Calories_from_carbohydrate )

my_function()

