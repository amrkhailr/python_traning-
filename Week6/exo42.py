dct = {1:[0, 1], 2:[2, 3], 3:[4, 5]} 
print(len(dct))
3
###############
dct = {1:[0, 1], 2:[2, 3], 3:[4, 5]} 
for k in dct: 
    print(k)
1
2
3
##############
set1 = set([10, 20, 30, 40]) 
set2 = set([40, 50, 60]) 
set3 = set1.union(set2)
print(set3)
{50, 20, 40, 10, 60, 30}
#############################
set1 = set(['o', 'p', 's', 'v']) 
set2 = set(['a', 'p', 'r', 's']) 
set3 = set1.intersection(set2) 
print(set3)
{'s', 'p'}
##################
set1 = set(['d', 'e', 'f']) 
set2 = set(['a', 'b', 'c', 'd', 'e']) 
set3 = set1.difference(set2) 
print(set3)
{'f'}
###########################
set1 = set([1, 2, 3]) 
set2 = set([2, 3, 4]) 
set3 = set1.symmetric_difference(set2)
print(set3)
{1, 4}
