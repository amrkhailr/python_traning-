#9. Write a program that uses nested loops to draw this pattern:
#*******
#******
#*****
#****
#***
#**
#*



for x in range(7, 0, -1):
    print("*" * x)
#===============================================

#and in nested loop:

lastnumber = 7

for n in range(0, lastnumber):
    for column in range(0,n+1):
        print ('*', end='')
    print("")
#=================================================

# OR 

for n in range(7,0, -1):
    for column in range(0, n-1):
        print ('*', end='')
    print("*")
    

 