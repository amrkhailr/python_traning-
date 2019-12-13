#count how many times a word is in a paragraph
#I am here today just because I am strong
#I=2 am=2 here=1 today=1 just=1 because=1 strong=1
#k={}

para='''I am here today just because I am strong''' 
arr = para.split()
#print(arr)
k={}
for word in arr:
    if word in k:
        k[word]=k[word]+1
    else:
        k[word]=1
print(k)
