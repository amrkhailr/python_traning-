import random

class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.position = None
    def display(self):
        print("My name is " + self.name + " I am " + str(self.age) + " old years, My position is " + str(self.position) )
    
    def setposition(self,position):
        self.position = position

class Engineer:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.position = None
    def display(self):
        print("My name is " + self.name + " I am " + str(self.age) + " old years, My position is " + str(self.position) )
    
    def setposition(self,position):
        self.position = position

#if __name__ == "__main__":
    #p=Student("Peter",18)
    #p.display()
    #p.setposition("Noc Eng.")
    #p.display()
    #p.position = "Auotmation"
    #p.display()