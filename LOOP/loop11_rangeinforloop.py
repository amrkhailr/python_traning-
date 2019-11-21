for num in range(5):
    print(num)

################# BOTH are the same but range is faster#####################
for num in [0, 1, 2, 3, 4]:
   print(num)

# OR

# This program demonstrates how the range
# function can be used with a for loop.
def main():
# Print a message five times.
   for x in range(5):
    print('Hello world!')
main()

##################################################

for num in range(1, 5):
  print(num)
This code will display the following:
1
2
3
4
#################################################
for num in range(1, 10, 2):
   print(num)
#In this for statement, three arguments are passed to the range function:
#The first argument, 1, is the starting value for the sequence.
#The second argument, 10, is the ending limit of the list. This means that the last number in the sequence will be 9.
#The third argument, 2, is the step value. This means that 2 will be added to each successive number in the sequence.This code will display the following:
1
3
5
7
9

# OR

for num in range(1, 10, 5):
    print(num)
1
6

# OR
for num in range(1, 10, 4):
    print(num)
1
5
9