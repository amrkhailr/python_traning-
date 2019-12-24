import re
string = "Christmas is too close, let go to visit santa cruz."

#string = "hi"
if re.search(r"...[.]$", string): # if chracter ends with .
    print('match')
else:
    print("not match")