#5. Kinetic Energy In physics, an object that is in motion is said to have kinetic energy (KE). 
#The following formula can be used to determine a moving object’s 
#kinetic energy: KE = 1⁄2 mv2 
# The variables in the formula are as follows: 
#KE is the kinetic energy in joules, m is the object’s mass in kilograms, and v is the object’s 
#velocity in meters per second. Write a function named kinetic_energy that accepts an object’s 
#mass in kilograms and velocity in meters per second as arguments. The function should return 
#the amount of kinetic energy that the object has. Write a program that asks the user to enter 
#values for mass and velocity, 
#and then calls the kinetic_energy function to get the object’s kinetic energy.

def main():
    print("Kinetic Energy")
    mass=int(input("Enter mass: "))
    velocity=int(input("Enter velocity: "))
    result = kinetic_energy(mass,velocity)
    print("kinetic energy: ", result)
def kinetic_energy(mass,velocity):
    print(mass/2*velocity**2)
main()
