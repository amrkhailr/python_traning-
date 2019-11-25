#4. Falling Distance The following formula can be used to determine the distance an object falls 
# due to gravity in a specific time period, starting from 
# rest: d = 1⁄2 gt2 
# The variables in the formula are as follows: d is the distance in meters, g is 9.8, 
# and t is the amount of time in seconds, that the object has been falling. 
# Write a function named falling_distance that accepts an object’s falling time in seconds as an 
# argument. 
# The function should return the distance in meters that the object has 
# fallen during that time interval. Write a program that calls the function in a loop that 
# passes the values 1 through 10 as arguments and displays the return value.

g = 9.8
def main():
    print("falling distance")
    for count in range(10):
        time = count + 1
        distance = falling_distance(time)
        print("Time: ",time,"distance: ",distance)
def falling_distance(t):
    print(g/2*t*t)

main()
