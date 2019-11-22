 #Average Rainfall
#Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The
#outer loop will iterate once for each year. The inner loop will iterate twelve times, once
#for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of
#months, the total inches of rainfall, and the average rainfall per month for the entire
#period.

total = 0

for n in range(int(input("Years:"))):
    for month in range(12):
        rain = float(input('inches of rain'))
        total = rain + total
    average = rain/month
    print('Years:',years+1,'Months:',months+1,'Rainfall total:',total,'Average Rainfall:',average)


