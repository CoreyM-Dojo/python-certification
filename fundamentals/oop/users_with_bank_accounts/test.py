from classes.user import User
from classes.account import BankAccount

user = User("Corey", "c@m.com")
# user.display_user_balance()
user.make_deposit(100)
user.display_user_balance()
user.display_user_balance("savings")
user.make_deposit(100, "savings")
user.display_user_balance("savings")
