#2. Calories Burned
#Running on a particular treadmill you burn 3.9 calories per minute. Write a program
#that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30
#minutes.

minutes = [10,15,20,25,30]
for x in range(10,35,5):
    print("You have burned" + str(x*minutes)+ "calories" + str(x) + "minutes")
