#Assume each of the variables set1 and set2 references a set. 
# Write code that creates another set containing all the elements of set1 and set2 and assigns the resulting set to the variable set3. 
set1 = {10,20,30}
set2 = {100,200,300}
set3 = set1.union(set2)
print(set3)
