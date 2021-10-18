"""
Programmer: William Bratz
Assignment: Module 7 - Assignment
Date Completed: 10/5/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

from product import Product

product_list = []

def main():
    loop = True
    while loop:
        product_name = input("Enter a product name: ")
        product_price = input("Enter a price for this product: ")
        product_discount_percent = input("Enter a discount percentage: ")
        continue_loop = input("Enter another product? (Enter y/n): ").lower()
        print()
        product_list.append(Product(product_name, float(product_price), int(product_discount_percent)))
        
        if(continue_loop != 'y'):
            loop = False
            
    print("PRODUCTS:")
    print("==========================")
    print()
    for product in product_list:
        print(product)
        print()
        
main()