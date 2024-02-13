class BankAccount():
    """A simple way to create a bank account"""

    def __init__(self,account_holder,account_number,balance,account_type):
        """Initializing account details"""
    
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
    
    def display_account_info(self):
         """Return account Information"""
         print(f"Account Information\n"
               f"Account Holder: {self.account_holder}\n"
               f"Account Number: {self.account_number}\n"
               f"Balance: {self.balance}\n"
               f"Account Type: {self.account_type}\n")
         
    def deposit(self, amount):
        """Allows users to deposit money into the account"""
        self.balance +=amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Allows users to withdraw money from the account"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient Balance. Withdrawal unseccessful")

# Creating instances for Bank Acccount
account1 = BankAccount("Comfort Kyeremeh","123456",20000,"Savings")
account2 = BankAccount("Andrews Kyeremeh","123457",50000,"Investment")

# Calling methods for each instance
account1.display_account_info()
account1.deposit(20000)
account1.withdraw(7000)

account2.display_account_info()
account2.deposit(30000000)
account2.withdraw(500)

    