class Product:
    
    def __init__(self, name, price, discount_percent):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent
                
    def discount_amount(self):
        return self.price * (self.discount_percent / 100)
    
    def discounted_price(self):
        return self.price - self.discount_amount()
    
    def __str__(self):
        return self.name+"\nPrice: $" + "{:.2f}".format(self.price)  + "\nDiscount Percent: " + str(self.discount_percent)+"%"+ "\nDiscount Amount: $" + "{:.2f}".format(self.discount_amount()) + "\nDiscount Price: $" + "{:.2f}".format(self.discounted_price())