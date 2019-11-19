def odd_even():
    Enter_number = int(input('Please enter your number '))
    if (Enter_number%2==0):
        print('Even')
    else:
        print('odd')
odd_even()
################################
a=10
while (a>0):
    print(a*2)
    a=a-1
######################################
a = int(input("give a number"))

while (a<100):
    print(a)
    a=a*2
####################################
a = int(input("Enter your number please"))

while a >= 10 and a <= 100:
    a = int(input("Enter your number please"))
    print(a)
###############################################
# for loop: do it for list and do it each one by one until all finished.

L = [10,12,16,17]

for n in L:
    print(n)
###############################################
L = [10,12,16,17]

for n in L:
    print(n+20)
###############################
L = [10,12,16,17]
x=2

for n in L:
    print("hello",n+x)
###################################
for n in range(10):
    print(n)
################################
for n in range(1,100,5):
    print(n)
##############################
for n in range(100,1,-1):
    print(n)
##################################
num=int(input("give a number :"))
for n in range(num):
    print(n)
###################################
S = 0
L = [1,5,3]
for n in L:
    S = S+n
print(S)
##################################
