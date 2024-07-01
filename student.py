from user import User

class StudentAccount(User):
    def __init__(self):
        User.__init__(self)

    def withdraw(self, amount):
        if amount < 2000:
            super().withdraw(amount)
        else:
            print("Amount exceeds limit")

    def deposit(self, amount):
        if amount < 50000:
            super().deposit(amount)
        else:
            print("Amount exceeds limit")

student = StudentAccount()
one = int(input("Select 1 for Withdraw or 2 for Deposit: "))

if one == 1:
    print("Withdrawal")
    amount = int(input("Enter Amount: "))
    student.withdraw(amount)
elif one == 2:
    print("Deposit")
    amount = int(input("Enter Amount: "))
    student.deposit(amount)
else:
    print("Option Not Available")
