#Write a program that opens an output file with the filename my_name.txt, writes your name to the file, and then closes the file.

file = open('myname.txt', 'w')
file.write('My name is Romal')
file.closed()

