#What will the following program display?
def main():
   x=1
   y=3.4
   print(x, y)
   change_us(x, y)
   print(x, y)

def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

main()


# Look at the following function definition:
#def my_function(a, b, c):
#d = (a + c) / b
#print(d)
#a. Write a statement that calls this function and uses keyword arguments to pass 2 into
#a, 4 into b, and 6 into c.
#b. What value will be displayed when the function call executes?

def my_function(a, b, c):
    d = (a+c) / b
    print(d)

my_function(2, 4, 6)

