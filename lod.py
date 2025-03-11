class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

class Customer:
    def __init__(self, name):
        self.name = name
        self.address = Address("123 Main St", "Boston")
        self.wallet = Wallet(1000)

class Wallet:
    def __init__(self, amount):
        self.amount = amount

class OrderProcessor:
    def process_order(self, customer, order_amount):
        # Violates LoD by reaching through multiple objects
        if customer.wallet.amount >= order_amount:
            customer.wallet.amount -= order_amount
            print(f"Shipping to {customer.address.street}, {customer.address.city}")
            return True
        return False
