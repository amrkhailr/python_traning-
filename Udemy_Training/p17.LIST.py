# Comperhensive LIST 

nums = [1,2,3]
[x*10 for x in nums]
[10, 20, 30]

### Or 

colors = ["yello", "blue", "red"]
[color.upper() for color in colors] # this comperhensive things we can do without using the for or while loop
['YELLO', 'BLUE', 'RED']

#### OR

nums = [1,2,3]
[str(num) for num in nums] # make it str 
['1', '2', '3']

#### OR

nums = [1,2,3]
[str(num)+ "HELLO" for num in nums]
['1HELLO', '2HELLO', '3HELLO']

#####
numbers = [1,2,3,4,5,6]

even = [num for num in numbers if num %2 ==0] # show me the even numbers 
odds = [num for num in numbers if num %2 !=0] # show me the odd numbers 

print(even)
print(odds)

[2, 4, 6]
[1, 3, 5]

#####

numbers = [1,2,3,4,5,6]
[num*2 if num % 2 == 0 else num/2 for num in numbers] # Multiply even numbers and divide odd numbers 
[0.5, 4, 1.5, 8, 2.5, 12]

#####
vowels = "This is so much fun"
''.join(char for char in vowels if char not in "aeiou") # remove vowel words 
'Ths s s mch fn'
######

'...'.join(["cool", "dude"]) # another example how to  join or add ... between indexes 
'cool...dude'
######





