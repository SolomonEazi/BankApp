from user import User

class CurrentAccount(User):
    def __init__(self):
        User.__init__(self)

current = CurrentAccount()
print("Press 1 to withdraw and 2 to deposit ")
one = int(input("Enter: "))

if one == 1:
    amount = int(input("Enter Amount: "))
    current.withdraw(amount)
elif one == 2:
    amount = int(input("Enter Amount: "))
    current.deposit(amount)
else:
    print("Thank you for Banking with us!")
