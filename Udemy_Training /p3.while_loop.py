#for num in range (1,11):
#    print(num)   This is a FOR LOOP which is much shorter 

# now we show the same example in WHILE LOOP

num = 1
while num < 11: 
    print(num)  # But this code will go forever after runnning it. Just to show myself a diffence 
    num += 1 # now we add one saying that add one for each number untill it reaches 11.





msg = input("password")
while msg != "bananas":
    print("Wrong")
    msg = input("password")
print("Correct")