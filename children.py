from user import User

class ChildrenAccount(User):
    def __init__(self):
        User.__init__(self)




children = ChildrenAccount()
# customer deposits
amount = int(input("How much do you want to deposit: "))
children.deposit(amount)
children.get_interest_rate(amount)
children.totalTwo()
