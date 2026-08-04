class BankAccount:
    def __init__(self):
        self.balance = 0

    def enter_money(self, amount):
        self.balance += amount
    
    def take_money(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance

    def take_money(self, amount):
        balance = self.balance
        if balance - amount>=self.min_balance:
            self.balance -= amount
        else:
            print("It is not possible to remove that amount, minimum amount must be kept")

my_dollars_account = SavingsAccount(20)
my_dollars_account2 = SavingsAccount(20)
print(f"Balance:{my_dollars_account.balance}")
print(f"Balance:{my_dollars_account2.balance}")
my_dollars_account.enter_money(100)
print(f"Balance:{my_dollars_account.balance}")
print(f"Balance:{my_dollars_account2.balance}")
my_dollars_account.take_money(20)
print(f"Balance:{my_dollars_account.balance}")
print(f"Balance:{my_dollars_account2.balance}")
my_dollars_account.take_money(80)
print(f"Balance:{my_dollars_account.balance}")
print(f"Balance:{my_dollars_account2.balance}")
