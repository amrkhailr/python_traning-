#the value 10 is specified as the seed value. If a program calls the random.
#seed function, passing the same value as an argument each time it runs, 
#it will always produce the same sequence of pseudorandom numbers. 
#To demonstrate, look at the following interactive sessions. 
#(We have added line numbers for easier reference.)

import random 
random.seed(10)
random.randint(1, 100)
random.randint(1, 100)
