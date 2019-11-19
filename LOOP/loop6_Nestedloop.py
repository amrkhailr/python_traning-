Nested Loops
CONCEPT: A loop that is inside another loop is called a nested loop.
A nested loop is a loop that is inside another loop. A clock is a good example of something
that works like a nested loop. The second hand, minute hand, and hour hand all spin
around the face of the clock. The hour hand, however, only makes 1 revolution for every
12 of the minute hand’s revolutions. And it takes 60 revolutions of the second hand for the
minute hand to make 1 revolution. This means that for every complete revolution of the
hour hand, the second hand has revolved 720 times. Here is a loop that partially simulates
a digital clock. It displays the seconds from 0 to 59:
for seconds in range(60):
print(seconds)
We can add a minutes variable and nest the loop above inside another loop that cycles
through 60 minutes:
for minutes in range(60):
for seconds in range(60):
print(minutes, ':', seconds)
To make the simulated clock complete, another variable and loop can be added to count the hours:
for hours in range(24):
for minutes in range(60):
for seconds in range(60):
print(hours, ':', minutes, ':', seconds)
Program 5-17 (continued)
38 print('Retail price: $', format(retail, ',.2f'))
39
40 # Call the main function.
41 main()
Program Output (with input shown in bold)
Enter the item's wholesale cost: –.50e
ERROR: the cost cannot be negative.
Enter the correct wholesale cost: 0.50e
Retail price: $1.25.
Do you have another item? (Enter y for yes): ne
5.7 Nested Loops 191
This code’s output would be:
0:0:0
0:0:1
0:0:2
(The program will count through each second of 24 hours.)
23:59:59
The innermost loop will iterate 60 times for each iteration of the middle loop. The middle
loop will iterate 60 times for each iteration of the outermost loop. When the outermost loop
has iterated 24 times, the middle loop will have iterated 1,440 times and the innermost loop
will have iterated 86,400 times! Figur