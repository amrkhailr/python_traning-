para=input("type a paragraph : ")
arr = para.split()
#print(arr)
k={}
for word in arr:
    if word in k:
        k[word]=k[word]+1
    else:
        k[word]=1
for key,val in k.items():
    print(key + " : " + str(val))
    