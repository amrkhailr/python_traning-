list = [[1,2,3,] , [4,5,6] , [7,8,9]] # nested list
list[0]
list[1]

####

list = [[1,2,3,] , [4,5,6] , [7,8,9]]
for num in list:
    print(num)
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

######

list = [[1,2,3,] , [4,5,6] , [7,8,9]]

for num in list:
    for list in num:
        print(list)

1
2
3
4
5
6
7
8
9

####

["*" for i in range(1,4)]
['*', '*', '*']


