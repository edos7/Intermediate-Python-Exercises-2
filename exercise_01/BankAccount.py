#Emir Dostovic 
#Used ChatGPT to figure out how to define classes in Python
class BankAccount:
    def __init__(self,account_name,starting_balance):
        self.account_name=account_name
        self.starting_balance=starting_balance
    def deposit(self, amount):
        self.starting_balance+=amount
    def withdraw(self,withdraw):
        self.starting_balance-=withdraw
    def get_balance(self):
        return f"{self.account_name} has a balance of {self.starting_balance}"