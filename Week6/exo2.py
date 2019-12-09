def main():
    print('Enter the names.')
    name1 = input('Friend 1: Type your thoughts')
    name2 = input('Friend 2: Type your thoughts')
    name3 = input('Friend 3: Type your thoughts')

    m = open('apogee.txt', 'w')

    m.write(name1 + ' \n')
    m.write(name2 + ' \n')
    m.write(name3 + ' \n')

    m.close()
    print('The names were written to file')
main()
