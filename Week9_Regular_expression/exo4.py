import re
string = "Christmas is too close, hello hello let go to visit santa cruz."

#string = "hi"
if re.search(r"hello?", string): # search for a chrater if exist 0 or one time
    print('match')
else:
    print("not match")