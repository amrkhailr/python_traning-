import re

#string = "Christmas is too close, let go to visit santa cruz"
string = "hi"
if re.search(r"...", string): # find if i have 3 chractires or more in the sentacen at string 
    print('I have 3 letters or more')
else:
    print("I have not 3 letters or more")
