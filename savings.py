from user import User

class Savings(User):
    def __init__(self):
        User.__init__(self)

    def withdraw(self, amount):
        if amount < 700000:
            super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded")

savings = Savings()
one = int(input("Select 1 for Withdraw or 2 for Deposit: "))

if one == 1:
    print("Withdrawal")
    amount = int(input("Enter Amount: "))
    savings.withdraw(amount)
elif one == 2:
    print("Deposit")
    amount = int(input("Enter Amount: "))
    savings.deposit(amount)
    savings.get_interest(amount)
    savings.totalOne()
else:
    print("Option Not Available")
