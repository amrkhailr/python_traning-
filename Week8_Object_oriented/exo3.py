class Pet:
    def __init__(self, name,animal_type, age ):
        self.__name = name
        self.__age = age
        self.__animal_type = animal_type
    def display(self):
        print("The animal name is " + self.__name + ". The animal age is " + str(self.__age) + " years old and the animal type is " + self.__animal_type )

if __name__ == "__main__":
    p=Pet("Dog",  "social animal",2)
    p.display()


    