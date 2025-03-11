class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        """Deposits money and returns new balance"""
        self.balance += amount
        return True  # Surprising: returns bool instead of balance
    
    def withdraw(self, amount):
        """Withdraws money if sufficient funds"""
        if self.balance >= amount:
            self.balance -= amount
            return amount
        return 0  # Surprising: returns 0 instead of indicating failure
    
    def transfer(self, target_account, amount):
        """Transfers money between accounts"""
        if self.withdraw(amount):
            target_account.deposit(amount)
            return None  # Surprising: no indication of success/failure

# Usage - Surprising behaviors
account1 = Account(1000)
account2 = Account(500)

print(account1.deposit(100))  # Prints True instead of new balance
print(account1.withdraw(2000))  # Prints 0 instead of indicating insufficient funds
account1.transfer(account2, 300)  # No way to know if transfer succeeded
