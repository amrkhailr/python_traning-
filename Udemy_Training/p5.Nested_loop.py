for x in range(3):
    for num in range (1,11):
        print("\U0001f600" * num)


# or we can do it this way too, without multification 

for num in range (1,11):
    count = 1
    smiley = ""
    while count <= num:
        smiley += "\U0001f600"
        count += 1
    print(smiley)