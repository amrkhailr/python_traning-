#A file exists on the disk named students.txt. 
# The file contains several records, and each record contains two fields: 
# (1) the student’s name, and (2) the student’s score for the final exam. 
# Write code that changes Julie Milan’s score to 100
import os
def main():
    found = False
    search = 'Julie Milan'
    infile = open('studnet.txt', 'r')
    temp = open('temp.txt', 'w')
    name = infile.readline()
    score = n
while name != score:
    score=int(infile.readline())
    name = name.rstrip('\n')
    if name != search:
        temp.write(name+'\n')
        temp.write(str(score)+ '\n')
    else:
        temp.write(name+'\n')
        temp.write('100' + '\n')
        found = True
    name = infile.readline()
infile.close()
temp.close()
os.remove('student.txt')
os.rename('temp.txt', 'student.txt')
if found:
    print('updated')
else:
    print('not found')
main()
