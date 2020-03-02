list = [1,2,3,4]
list[1:] # this will slice our list and give us an output after 2. 

###

list = [1,2,3,4]
list[1:3] # slice from 1 to index 3

####

list = [1,2,3,4]
list[1::3] # slice from 1 to index 3 and then go infinity and dont stop 

####

list = [1,2,3,4]
list[::2] # skip each index 2 time and output the third ones 

#####

names = ["Romal", "Aimal"]

names[0], names[1] = names[1], names[0] # switching or shuflling indexs or itmes 

print(names)
names = ["Aimal", "Romal"]