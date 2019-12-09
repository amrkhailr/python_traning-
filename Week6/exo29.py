fn = input("gice a file name")
with open (fn, "r") as f:
    c= f.read()
    c=c.splitlines()
    k=c[:5]
    for i in k:
        print(i)
