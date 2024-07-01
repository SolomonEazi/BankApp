class User:
    def __init__(self):
        self.balance = 1000
        self.__interest_rate = (0.7 / 100)
        self.__interest = (0.5 / 100)

    def get_interest_rate(self, amount):
        self.__interest_rate = self.__interest_rate * amount
        return print("Interest:", self.__interest_rate)

    def get_interest(self, amount):
        self.__interest = self.__interest * amount
        return print ("Interest:", self.__interest)



    def deposit(self, amount):
        self.balance = amount + self.balance
        print("BHU Credit Alert")
        print("Credit:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("BHU Debit Alert")
        print("Debit:", amount)
        print("Balance:", self.balance)

    def totalOne(self):
        total = self.balance + self.__interest
        return print("New balance:", total)

    def totalTwo(self):
        total = self.balance + self.__interest_rate
        return print("New balance is:", total)
