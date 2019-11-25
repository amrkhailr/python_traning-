#6. Test Average and Grade Write a program that asks the user to enter five test scores. 
#The program should display a letter grade for each score and the average test score. 
#Write the following functions in the program: 
#• calc_average—This function should accept five test scores as arguments and return the average of 
#the scores. • determine_grade—This function should accept a test score as an argument and return a 
#letter grade for the score, based on the following grading scale:

#Score Letter Grade 90–100 A 80–89 B 70–79 C 60–69 D Below 60 F

def main():
    print("Test average score")
    sc1 = int(input("Enter first score"))
    print("Your grade: ", determine_grade(sc1))
    sc2 = int(input("Enter second score"))
    print("Your grade: ", determine_grade(sc2))
    sc3 = int(input("Enter third score"))
    print("Your grade: ", determine_grade(sc3))
    sc4 = int(input("Enter forth score"))
    print("Your grade: ", determine_grade(sc4))
    sc5 = int(input("Enter fift score"))
    print("Your grade: ", determine_grade(sc5))
    average = calc_average(sc1,sc2,sc3,sc4,sc5)
    print("Your average score", average)
def calc_average(sc1,sc2,sc3,sc4,sc5):
    total = sc1+sc2+sc3+sc4+sc5
    average = total/5
    print(average)
def determine_grade(score):
    if score >= 90:
        print('A')
    elif score >=80 and score < 90:
        print('B')
    elif score >=70 and score <80:
        print('C')
    elif score >=60 and score <70:
        print('D')
    else:
        print('F')
main()