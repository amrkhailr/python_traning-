class Youtube_account:
    def __init__(Self, History, age, GDP):
        self.History = History
        self.age = age
        self.GDP = GDP
    def display(self):
        print("The company name is  " + self.History + " it has been 16 " + str(self.age) + " in the market and it makes around 7.6 " + str(self.GDP) +"amount of money")

if __name__ == "__main__":
    p=Youtube_account("Youtube", 19 ,7)
    p.display()
    