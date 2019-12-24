import re
string = "Christmas is too close, let go to visit santa cruz."

#string = "hi"
if re.search(r"l+", string): # search for if L repeated multiple times 
    print('match')
else:
    print("not match")