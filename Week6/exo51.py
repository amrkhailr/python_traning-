# Assume the variable dct references a dictionary. 
# Write code that pickles the dictionary and saves it to a file named mydata.dat.

import pickle
set = {1:'aaa',2:'bbb'}
file1 = open('mydata123.dat','wb')
wr = pickle.dump(set, file1)
file1.close()
