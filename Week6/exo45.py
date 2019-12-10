#Assume the variable dct references a dictionary. 
# Write an if statement that determines whether the key 'James' exists in the dictionary. If so, display the value that is associated with that key. If the key is not in the dictionary, display a message indicating so

dct = {'James':1}
if 'James' in dct:
    print(dct['James'])
else:
    print('Not found')
