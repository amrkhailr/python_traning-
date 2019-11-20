#1. Write a while loop that lets the user enter a number. The number should be multiplied
#by 10, and the result assigned to a variable named product. The loop should iterate as
#long as product is less than 100

number = 100
enternumber = int(input('please enter a number'))
while enternumber < 100 :
    total = enternumber * 10
    print('Your total number is',total)
    enternumber = int(input('please enter a number'))


