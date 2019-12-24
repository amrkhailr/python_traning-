import re
string = "Christmas is too close, let go to visit santa cruz."

#string = "hi"
if re.search(r"[^cC].*", string): # search for a chriater starts by p and then many times
    print('match')
else:
    print("not match")