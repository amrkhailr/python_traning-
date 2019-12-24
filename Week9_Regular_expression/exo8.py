import re
#string = "Christmas is too close, let go to visit santa cruz."

string = "hi tc"
if re.search(r"(Hello|Hi|Pogo)", string): # if any of the chracter exist in string 
    print('match')
else:
    print("not match")