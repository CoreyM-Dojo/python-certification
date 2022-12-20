from classes.account import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = BankAccount(0.01)
        self.savings = BankAccount(0.03)

    def make_deposit(self, amount, account="checking"):
        getattr(self, account).deposit(amount)

    def make_withdrawal(self, amount, account="checking"):
        if self.getattr(self, account) - amount >= 0:
            self.getattr(self, account).withdraw(amount)

    def display_user_balance(self, account="checking"):
        print(f"{self.name}: {getattr(self, account).balance}")

    def make_transfer(
        self, other, amount, account="checking", target_account="checking"
    ):
        if getattr(self, account).balance - amount >= 0:
            getattr(self, account).withdraw(amount)
            getattr(self, account).deposit(amount)
        else:
            print("Insufficient funds for transfer")
