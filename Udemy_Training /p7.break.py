while True:
    command = input("type EXit to exit")
    if command == exit: 
        break 

# or 

for x in range (1,11):
    print (x)
    if x == 3:
        break 

# Or for lines 

times = int(input("how many times do I have to tell you? "))
for time in range(times):
    print("clean your room")
    if time <= 3:
        print ("Do you even listen? ")
        break

# 
from random import randint

number = 0 # store number in here, each time through 
i = 0 # store it here for i 

while number != 5: # Keep looping while number is not 5
    i += 1 # should be incremented by 1
    number = randint(1 ,10) # update number to be a new random int from 1 - 10