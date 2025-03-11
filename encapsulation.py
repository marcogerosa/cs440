class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transaction_history = []
        self.interest_rate = 0.01
        self.account_type = "savings"
    
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

# Usage - Direct access to internal state
account = BankAccount(1000)
account.balance -= 500  # Directly modifying balance
account.interest_rate = 0.05  # Directly changing interest rate
account.transaction_history.append({"type": "withdrawal", "amount": 500})  # Directly modifying history
