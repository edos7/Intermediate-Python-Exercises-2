from BankAccount import BankAccount

account=BankAccount("Checking",100)
account.deposit(100)
account.withdraw(40)
print(account.get_balance())
