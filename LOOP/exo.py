# Some good listens before we stat LOOP!:
#Python List

#Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type
#The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.
#Creating a list is as simple as putting different comma-separated values between square brackets. For example −
# Below are all list examples:
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5];
list3 = ["a", "b", "c", "d"]

#Accessing Values in Lists= IN PYTHON LISTS Starts with 0 and goes to ----.....

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5] #excute list2 index 1 through 5.
#When the above code is executed, it produces the following result −
list1[0]  => physics
list2[1:5]  => [2, 3, 4, 5]
#or 
switches=[2960,3815,'N2000','N3000']
print(switches[0])
2960
switches[2:3]
['N2000']
switches[1:3]
[3815, 'N2000']
switches[0:3]
[2960, 3815, 'N2000']
switches[-1]
'N3000'
switches[-3:-1]
[3815, 'N2000']
switches[-3:]
[3815, 'N2000', 'N3000']

#Updating Lists
#You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator, and you can add to elements in a list with the append() method. For example −

list = ['physics', 'chemistry', 1997, 2000];
print "Value available at index 2 : "
print list[2]
list[2] = 2001;
print "New value available at index 2 : "
print list[2]
#When the above code is executed, it produces the following result −
#Value available at index 2 :
1997
#New value available at index 2 :
2001

#Delete List Elements
#To remove a list element, you can use either the del statement if you know exactly which element(s) you are deleting or the remove() method if you do not know. 


list1 = ['physics', 'chemistry', 1997, 2000];
print list1
del list1[2];
print "After deleting value at index 2 : "
print list1
#When the above code is executed, it produces following result −
['physics', 'chemistry', 1997, 2000]
#After deleting value at index 2 :
['physics', 'chemistry', 2000]

##########################Basic List Operations#######################
#Lists respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string.
#In fact, lists respond to all of the general sequence operations we used on strings in the prior chapter.
#Python Expression	Results	Description
len([1, 2, 3])	3	Length
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
3 in [1, 2, 3]	True	Membership
for x in [1, 2, 3]: print x,	1 2 3	Iteration


##########################Indexing, Slicing, and Matrixes############################
Because lists are sequences, indexing and slicing work the same way for lists as they do for strings.
Assuming following input −
 L = ['spam', 'Spam', 'SPAM!']


Python Expression	Results	Description
L[2]	SPAM!	Offsets start at zero #(From left indexes starts with 0)
L[-2]	Spam	Negative: count from the right #(when you start indexes from right in python, they starts with -)
L[1:]	['Spam', 'SPAM!']	Slicing fetches sections #(start from 1 and then go on)












