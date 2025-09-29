# # class BankAccount:
# #     def __init__(self, name, amount):
# #         self.name = name
# #         self.amount = amount

# #     def calculate_interest(self, rate):
# #         self.amount= (self.amount*rate)/100 + self.amount
    
# #     def deposit(self, amount, rate):
# #         self.amount = self.amount+(amount-(amount*(rate/100)))
        
# #     def withdraw(self, amount, rate):
# #         if amount>self.amount:
# #             print("Add some money before withdrawing")
# #             return
# #         self.amount = self.amount-(amount)
# #         self.amount = self.amount-(amount*(rate/100))

        
# #     def __str__(self):
# #         return str(self.amount)
    
# #     class subAccount:
# #         parent_id=""
    
# # my_account=BankAccount('Amine', 100)
# # my_account.calculate_interest(2.5)
# # print(my_account)
# # my_account.deposit(1000, 0.3)
# # print(my_account)
# # my_account.withdraw(5000, 1)
# # print(my_account)
# # my_account.subAccount().parent_id


# class Product:
#     title: str
#     desc: str
#     price: float
#     quantity: int

#     def __init__(self, title, price, quantity):
#         self.title, self.price, self.quantity = title, price, quantity

#     def __str__(self):
#         return self.title
    

# class Cart:
#     products: list[Product] = []
#     total: float

#     def add(self, product:Product):
#         self.products.append(product)


#     def remove(self, product:Product):
#         product_name = product.title
#         for prd in self.products:
#             if product_name==prd.title:
#                 self.products.remove(prd)
                
#     def get_total(self):
#         self.total=0
#         for prd in self.products:
#             self.total = self.total + prd.price

#         return self.total


# product1 = Product(title='test product1', price=1000, quantity=10)
# product2 = Product(title='test product2', price=1000, quantity=10)
# product3 = Product(title='test product3', price=1000, quantity=10)
# product4 = Product(title='test product4', price=1000, quantity=10)
# mycart=Cart()
# print(mycart.products)
# mycart.products = [
#     product1,
#     product2,
#     product3,
# ]
# print(mycart.products)
# mycart.add(product4)
# print(mycart.products)
# mycart.remove(product1)
# print(mycart.products)
# print(mycart.get_total())

class Employee:
    salary=0
    name=""
    position = ""
    parent: any = None
    is_parent=False

    def __init__(self, salary, position, name, is_parent=False):
        self.salary, self.position, self.name, self.is_parent=salary, position, name, is_parent

    def calclate_insurance(self, rate):
        return self.salary*rate/100

    def deduct_from_salary(self, days):
        amount=(self.salary/30)*days
        return self.salary-amount
    
    def benifits(self, benifit):
        return self.salary + benifit
    
my_employee=Employee(1000, 'manager', 'test', True)
insr_payment= my_employee.calclate_insurance(25)
print(insr_payment)

nd_employee=Employee(500, 'simple', 'test two')
nd_employee.parent=my_employee