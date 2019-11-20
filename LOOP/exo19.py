#10. Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #
#     #

for n in range(7):
    print('#', end="", sep="")
    for spaces in range(n):
        print(" ", end="", sep="")
    print("#", sep="")