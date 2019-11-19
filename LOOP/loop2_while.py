#The while Loop: a Condition-Controlled Loop

#CONCEPT: A condition-controlled loop causes a statement or set of statements to repeat as long as a condition is true. 
#In Python you use the while statement to write a condition-controlled loop.
#The while loop gets its name from the way it works: while a condition is true, do some task. 
#The loop has two parts: (1) a condition that is tested for a true or false value, 
#and (2) a statement or set of statements that is repeated as long as the condition is true. Figure 5-1 shows the logic of a while loop.

 
Infinite Loops
In all but rare cases, loops must contain within themselves a way to terminate. 
This means that something inside the loop must eventually make the test condition false. 
The loop in Program 5-1 stops when the expression keep_going == 'y' is false. If a loop does not have a way of stopping, it is called an infinite loop. 
An infinite loop continues to repeat until the program is interrupted. 
Infinite loops usually occur when the programmer forgets to write code inside the loop that makes the test condition false. 
In most circumstances you should avoid writing infinite loops.
