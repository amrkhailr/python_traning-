#1. Bug Collector
#A bug collector collects bugs every day for seven days. Write a program that keeps a running total of the number of bugs collected during the seven days. The loop should ask for
#the number of bugs collected for each day, and when the loop is finished, the program
#should display the total number of bugs collected.


total = 0
for day in range(7):
    bugs=int(float(input("how many bugs collected today ? ")))
    print("You have collected fortoday" + str(bugs))
    total = total + bugs
print("the total bugs collected duing the week is " + str(total))
