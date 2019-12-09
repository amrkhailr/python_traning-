def main():
    try:
        p = int(input('Give the number'))
        n=100/p
        print(n)
    except ZeroDivisionError:
        print('P must be different to zero')
main()