#7. Book Club Points
#Serendipity Booksellers has a book club that awards points to its customers based on the
#number of books purchased each month. The points are awarded as follows:
#• If a customer purchases 0 books, he or she earns 0 points.
#• If a customer purchases 1 book, he or she earns 5 points.
#• If a customer purchases 2 books, he or she earns 15 points.
#• If a customer purchases 3 books, he or she earns 30 points.
#• If a customer purchases 4 or more books, he or she earns 60 points.
#Write a program that asks the user to enter the number of books that he or she has purchased this month and displays the number of points awarded.

purchased_book = int(input('Enter the number of book you purchased this month: '))

if purchased_book == 0:
    print('Based on your purchase history you have 0 points')
elif purchased_book == 1:
    print('Based on your purchase history you earns 5 points')
elif purchased_book == 2:
    print('Based on your purchase history you earns 15 points')
elif purchased_book == 3:
    print('Based on your purchase history you earns 30 points')
elif purchased_book >= 4:
    print('Based on your purchase history you earns 60 points')



