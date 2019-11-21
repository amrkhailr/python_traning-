Infinite Loops (Basicall a loop with no NO and it just pops up aster each excution with the same statement)
In all but rare cases, loops must contain within themselves a way to terminate. This means
that something inside the loop must eventually make the test condition false. The loop in
Program 5-1 stops when the expression keep_going == 'y' is false. If a loop does not
have a way of stopping, it is called an infinite loop. An infinite loop continues to repeat
until the program is interrupted. Infinite loops usually occur when the programmer forgets
to write code inside the loop that makes the test condition false. In most circumstances you
should avoid writing infinite loops.
Program 5-3 demonstrates an infinite loop. This is a modified version of the commission
calculating program shown in Program 5-1. In this version, we have removed the code that
modifies the keep_going variable in the body of the loop. Each time the expression
keep_going == 'y' is tested in line 7, keep_going will reference the string ‘y’. As a consequence, the loop has no way of stopping. (The only way to stop this program is to press
Ctrl+C on the keyboard to interrupt it.)
Program 5-3 (infinite.py)
1 # This program demonstrates an infinite loop.
2 def main():
3 # Create a variable to control the loop.
4 keep_going = 'y'
5
6 # Warning! Infinite loop!
7 while keep_going == 'y':
8 # Get a salesperson's sales and commission rate.
9 sales = float(input('Enter the amount of sales: '))
10 comm_rate = float(input('Enter the commission rate: '))
11
12 # Calculate the commission.
13 commission = sales * comm_rate
14
15 # Display the commission.
16 print('The commission is $', \
17 format(commission, ',.2f'), sep='')
18
19 # Call the main function.
20 main()