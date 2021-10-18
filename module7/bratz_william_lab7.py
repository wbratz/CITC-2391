"""
Programmer: William Bratz
Assignment: Module 7 - Lab
Date Completed: 10/5/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

## Create product class
class Product:
    
    def __init__(self, name, price, discount_percent):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent
                
    def discount_amount(self):
        return self.price * (self.discount_percent / 100)
    
    def discounted_price(self):
        return self.price - self.discount_amount()

## instansiate 2 products with different values  
product1 = Product("Product 1", 11.00, 10)
product2 = Product("Product 2", 25.20, 15)

## print products with values
print("Product Data Name: " + product1.name + "\nPrice: $" + "{:.2f}".format(product1.price) + "\nDiscount Percent: " 
      + str(product1.discount_percent) + "\nDiscount Amount: " + str(product1.discount_amount()) + "\nDiscount Price: $" 
      + "{:.2f}".format(product2.discounted_price()))
print()
print("Product Data Name: " + product2.name + "\nPrice: $" + "{:.2f}".format(product2.price)  + "\nDiscount Percent: " 
      + str(product2.discount_percent) + "\nDiscount Amount: " + str(product2.discount_amount()) + "\nDiscount Price: $" 
      + "{:.2f}".format(product2.discounted_price()))
    