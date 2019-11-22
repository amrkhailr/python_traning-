def sum(tax,interest,amount):
    total = amount *tax + amount
    total = total*interest+total
    return total

def Hello():
    print("Hello everyone")
    
if __name__ =="__main__":
    Hello()
    a=float(input("Give the total money to borrow"))
    b=0.2
    c=float(input("give the bank interest: "))

    d = sum(b,c,a) #b is tax, c is interest, a is amount
    print("total to pay is: $"+ str(d))
 ##############################################################################
 test = 'n'
while (test != "y"):
    print("i am different")
    test=str(input("Would you like to live? y/n")
##########################################################
test = 5
while (test < 10):
    print(test, "is less than 10")
    test +=1
#######################################################
while
for
a=[1,3,4,5,6,"banana", "orange"]

len(a) => 7
a[0]
a[6],a[-1],
a[0:5], a[2:6],
################################################
minutes = [10,15,20,25,30]
for x in range(10,35,5):
    print("You have burned" + str(x*3.9)+ "calories" + str(x) + "minutes")
############################################
#minutes = [10,15,20,25,30]
#for b in range(10,35,5):
x=10
while(x<40):
    print("You have burned" + str(b*3.9)+ "calories" + str(b) + "minutes")
    x+=5
#####################################
test = 5
while (test < 10):
    print(test, "is less than 10")
    test +=1
###################################
test = 100
while (test < 0):
    print(test, "is less than 10")
    test -=1
#################################
a = [1,2,3,4,5]
for x in a:
    print(x)
##############################
a = [1,2,3,4,5]
for x in a:
    print(x*5)
############################
a = [1,2,3,4,5]
for x in a:
    print(x*5)
########################
a = [1,2,3,4,5]
for x in range(10,15,2):
    print(x*5)
#########################
total = 0
for day in range(7):
    bugs=int(float(input("how many bugs collected today ? ")))
    print("You have collected fortoday" + str(bugs))
    total = total + bugs
print("the total bugs collected duing the week is " + str(total))
#######################################################
minutes = [10,15,20,25,30]
for x in range(10,35,5):
    print("You have burned" + str(x*minutes)+ "calories" + str(x) + "minutes")
########################################################
write a program that runs a loop from 1 to 10
)dispaly tic if a number is diviable by 5
)disaply tac if a number is disivible by 3
)dispaly titac if a number is devidibel by 3 and 5