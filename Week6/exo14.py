
#A file exists on the disk named students.txt. 
# The file contains several records, and each record contains two fields: 
# (1) the student’s name, and (2) the student’s score for the final exam. Write code that deletes the record containing “John Perz” as the student name

import os

def main():
    found = False
    delete = 'John Perz'
    infile = open('student.txt', 'r')
    temp_file =open('temp.txt', 'w')
    name = infile.readline()
    while name != '':
        score = infile.readline()
        score=score.rstrip('\n')
        name=name.rstrip('\n')
    if name != delete:
        temp_file.write(name+'\n')
        temp_file.write(str(score)+'\n')
    else:
        found=True
        name=infile.readline()
        infile.close()
        temp_file.close()
        os.remove('infile')
        os.rename('temp.txt', 'student.tx')
    if found:
        print('Deleted')
    else:
        print('no exist')
main()
