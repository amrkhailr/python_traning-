#Assume each of the variables set1 and set2 references a set. 
# Write code that creates another set containing only the elements 
# that are found in both set1 and set2 and assigns the 
# resulting set to the variable set3.

set1 = {10,20,30,40,50,60}
set2 = {10,30,50,70,90}
set3 = set1.intersection(set2)
print(set3)
