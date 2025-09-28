class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def calculate_interest(self, rate):
        self.amount= (self.amount*rate)/100 + self.amount
    
    def deposit(self, amount, rate):
        self.amount = self.amount+(amount-(amount*(rate/100)))
        
    def withdraw(self, amount, rate):
        self.amount = self.amount-(amount)
        self.amount = self.amount-(amount*(rate/100))
        