class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account_balance - amount >= 0:
            self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}: {self.account_balance}")
        return self

    def make_transfer(self, other, amount):
        if self.account_balance - amount >= 0:
            self.account_balance -= amount
            other.account_balance += amount
        else:
            print("Insufficient funds for transfer")
        return self


mike = User("Mike", "mkultra@gmail.com")
kaleigh = User("Kaleigh", "kbaby@gmail.com")
cam = User("Cam", "camaroSS@gmail.com")

mike.make_deposit(20).make_deposit(200).make_deposit(350).make_withdrawal(
    100
).make_withdrawal(20).display_user_balance()

kaleigh.make_deposit(1000).make_deposit(135).make_withdrawal(35).make_withdrawal(
    100
).display_user_balance()

cam.make_deposit(10000).make_withdrawal(500)
cam.make_withdrawal(2000).display_user_balance()

mike.make_transfer(cam, 100).display_user_balance()
cam.display_user_balance()
