#f=open("apogee,txt", 'r')
#print(f.read())
#f.close()
#print("bye bye!!!")

with open("apogee.txt", 'r') as f:
    arr=f.read()
    arr=arr.splitlines()
    for line in arr:
        x=line.split(',')
        print(x[0] + ' ' + x [2])
print("bye bye !!!")