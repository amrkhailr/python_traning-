#Write code that retrieves and unpickles the dictionary that you pickled in Algorithm Workbench 11.

import pickle
file1 = open('mydata123.dat', 'rb')
wr = pickle.load(file1)
file1.close()

