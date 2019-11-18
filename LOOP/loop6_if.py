The for Loop: a Count-Controlled Loop
CONCEPT: A count-controlled loop iterates a specific number of times. In Python
you use the for statement to write a count-controlled loop.
As mentioned at the beginning of this chapter, a count-controlled loop iterates a specific
number of times. Count-controlled loops are commonly used in programs. For example,
main()
keep_going == 'y'
False
Return
True
Prompt the user: 'Do you
want to calculate another
commission? (Enter y for
yes)' and assign the input
to keep_going.
Assign 'y' to keep_going
show_commission( )
commission = sales *
comm_rate
Prompt the user to enter
the amount of sales and
assign it to sales.
Prompt the user to enter
the commission rate and
assign it to comm_rate.
Display the
commission
show_commission( )
Return

The for Loop
168 Chapter 5 Repetition Structures
suppose a business is open six days per week, and you are going to write a program that
calculates the total sales for a week. You will need a loop that iterates exactly six times.
Each time the loop iterates, it will prompt the user to enter the sales for one day.
You use the for statement to write a count-controlled loop. In Python, the for statement
is designed to work with a sequence of data items. When the statement executes, it iterates
once for each item in the sequence. Here is the general format:
for variable in [value1, value2, etc.]:
statement
statement
etc.
We will refer to the first line as the for clause. In the for clause, variable is the name of
a variable. Inside the brackets a sequence of values appears, with a comma separating each
value. (In Python, a comma-separated sequence of data items that are enclosed in a set of
brackets is called a list. In Chapter 8 you will learn more about lists.) Beginning at the next
line is a block of statements that is executed each time the loop iterates.
The for statement executes in the following manner: The variable is assigned the first
value in the list, and then the statements that appear in the block are executed. Then,
variable is assigned the next value in the list, and the statements in the block are executed again. This continues until variable has been assigned the last value in the list.
Program 5-5 shows a simple example that uses a for loop to display the numbers 1
through 5