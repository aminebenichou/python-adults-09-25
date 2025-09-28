class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def calculate_interest(self, rate):
        self.amount= (self.amount*rate)/100 + self.amount
    
    def deposit(self, amount, rate):
        self.amount = self.amount+(amount-(amount*(rate/100)))
        
    def withdraw(self, amount, rate):
        if amount>self.amount:
            print("Add some money before withdrawing")
            return
        self.amount = self.amount-(amount)
        self.amount = self.amount-(amount*(rate/100))

        
    def __str__(self):
        return str(self.amount)
    
    class subAccount:
        parent_id=""
    
my_account=BankAccount('Amine', 100)
my_account.calculate_interest(2.5)
print(my_account)
my_account.deposit(1000, 0.3)
print(my_account)
my_account.withdraw(5000, 1)
print(my_account)
my_account.subAccount().parent_id


class Product:
    title: str
    desc: str
    price: float
    quantity: int


class Cart:
    products: list[Product]


    def add(self, product:Product):
        self.products.append(product)
        

