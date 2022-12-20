class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    @classmethod
    def display_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("insufficient funds")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


account1 = BankAccount(0.01)
account2 = BankAccount(0.03)

account1.deposit(100).deposit(300).deposit(800).withdraw(
    200
).yield_interest().display_account_info()
account2.deposit(500).deposit(1000).withdraw(100).withdraw(200).withdraw(200).withdraw(
    0
).yield_interest().display_account_info()
BankAccount.display_accounts()
