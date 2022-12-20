class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        if self.account_balance - amount >= 0:
            self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name}: {self.account_balance}")

    def make_transfer(self, other, amount):
        if self.account_balance - amount >= 0:
            self.account_balance -= amount
            other.account_balance += amount
        else:
            print("Insufficient funds for transfer")


mike = User("Mike", "mkultra@gmail.com")
kaleigh = User("Kaleigh", "kbaby@gmail.com")
cam = User("Cam", "camaroSS@gmail.com")

mike.make_deposit(20)
mike.make_deposit(200)
mike.make_deposit(350)
mike.make_withdrawal(100)
mike.make_withdrawal(20)
mike.display_user_balance()

kaleigh.make_deposit(1000)
kaleigh.make_deposit(135)
kaleigh.make_withdrawal(35)
kaleigh.make_withdrawal(100)
kaleigh.display_user_balance()

cam.make_deposit(10000)
cam.make_withdrawal(500)
cam.make_withdrawal(2000)
cam.display_user_balance()

mike.make_transfer(cam, 100)
mike.display_user_balance()
cam.display_user_balance()
