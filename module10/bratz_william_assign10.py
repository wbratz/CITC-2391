"""
Programmer: William Bratz
Assignment: Module 10 - Lab
Date Completed: 10/28/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

class Person:
    
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def get_information():
        pass

class Customer(Person):

    def __init__(self, first_name, last_name, email_address, customer_number):
        super().__init__(first_name, last_name, email_address)
        self.customer_number = customer_number

    def get_information(self):
        return "Customer: " + self.first_name + " " + self.last_name + "\nCustomer Email: " + self.email_address + "\nCustomer Number: " + self.customer_number

class Employee(Person):
    
    def __init__(self, first_name, last_name, email_address, ssn):
        super().__init__(first_name, last_name, email_address)
        self.ssn = ssn

    def get_information(self):
        return "Employee: " + self.first_name + " " + self.last_name + "\nEmployee Email: " + self.email_address + "\nEmployee Number: " + self.ssn

def display(obj):
    
    if isinstance(obj, Customer):
        print("CUSTOMER INFORMATION:")
    else:
        print("EMPLOYEE INFORMATION:")

    print()

    print(obj.get_information())
    
#method to create a person since the spitit of this is that we're don't know which person we're creating
def create_person_type(first_name, last_name, email, person_type, number):
    if person_type == "c":
        return Customer(first_name, last_name, email, number)
    else:
        return Employee(first_name, last_name, email, number)


def main():

    continue_loop = True

    while continue_loop:
        first_name = input("Enter a first name: ")
        last_name = input("Enter a last name: ")
        email = input("Enter email address: ")
        type_of_person = input("Customer or employee? (c/e): ").lower()
        number = ""
        if type_of_person == "c":
            number = input("Enter customer number: ")

        else:
            number = input("Enter SSN: ")

        person = create_person_type(first_name, last_name, email, type_of_person, number)
        print()
        display(person)
        print()

        user_input = input("Continue? (y/n): ").lower()
        print()
        if user_input == "n":
            continue_loop = False

        print()
        

main()
