for num in range(1,21):
    if num == 4 or num == 13:
        print(num, "is unluck")
    elif num % 2 == 0 :
        print(num, "is even")
    else:
        print(num, "is odd")

# OR we can make our code very short:

for num in range(1,21):
    if num == 4 or num == 13:
        state = "unluck"
    elif num % 2 == 0 :
        state = "evem"
    else:
        state = "odd"
    print(num, "is" ,state)