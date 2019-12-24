import re
string = "Christmas is too close, let go to visit santa cruz."

#string = "hi"
if re.search(r"...[.]", string): # find a word with three chrachters and it should end with .
    print('match')
else:
    print("not match")