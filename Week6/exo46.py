#Assume the variable dct references a dictionary. 
# Write an if statement that determines 
# whether the key 'Jim' exists in the dictionary. 
# If so, delete 'Jim' and its associated value.

dct = {'jim':123}
if 'jim' in dct:
    dct.pop('jim')
print(dct)
