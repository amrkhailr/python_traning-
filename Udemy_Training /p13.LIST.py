data = [1,2,3]
data.append("6") ### .append is used for adding single item in our list 
print(data)

###

data = [1,2,3] # adding more items use .Extend
data.extend([6,7,8])
print(data)

####
list = [1,2,3,4]     
list.insert(2,'Hi')  # insert is used for to insert item at given position. 
print(list)