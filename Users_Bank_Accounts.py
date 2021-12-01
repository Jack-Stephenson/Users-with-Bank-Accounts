class BankAccount:
    #dont forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0):
        self.balance = balance
        self.interest = int_rate
    def deposit(self, amount):
        self.balance += amount
        print(f"Added ${amount}")
        print("Balance: $" + str(self.balance))
        return self
    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}")
            print("Balance: $" + str(self.balance))
        else:
            self.balance -= 5
            print(f"Error trying to withdraw ${amount}")
            print("Insufficient Funds: Charging a $5 fee")
            print("Balance: $" + str(self.balance))
        return self
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self
    def yield_interest(self):
        gain = self.balance * self.interest
        if self.balance > 0:
            print(f"Yielded ${gain} from interest!")
            self.balance += self.balance * self.interest
            print("Balance: $" + str(self.balance))
        else:
            print("Error: Balance too low to Yield Interest.")
            print("Balance: $" + str(self.balance))
        return self
jack = BankAccount(0.2, 800)
sam = BankAccount(0.21, 2000)

# jack.deposit(111).deposit(222).deposit(333).withdraw(3000).yield_interest().display_account_info()

# sam.deposit(117).deposit(151).withdraw(420).withdraw(365).withdraw(222).withdraw(334).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.account = BankAccount()
        self.name = name
        self.email = email
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self

user1 = User("user1", "user1@user1.com")
user1.make_deposit(111).make_deposit(222).make_deposit(333).make_withdrawal(200).display_user_balance()

user2 = User("user2", "user2@user2.com")
user2.make_deposit(200).make_deposit(100).make_withdrawal(300).make_withdrawal(200).display_user_balance()

user3 = User("user3", "user3@user3.com")
user3.make_deposit(1000).make_withdrawal(122).make_withdrawal(322).make_withdrawal(120).display_user_balance()
