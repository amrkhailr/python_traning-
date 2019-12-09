with open("apogee1.txt", 'w') as f:
    for line in range(5):
        x = input("type a name ")
        f.write(x+'\n')
print("bye bye !!!")