import re
string = "Christmas is too close, let go to visit santa cruz."

#string = "hi"
if re.search(r"e(mkhdh)*o", string): # search for chracter that followed by e and anything in between but ends with o
    print('match')
else:
    print("not match")