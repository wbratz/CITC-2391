"""
Programmer: William Bratz
Assignment: Module 9 - Lab
Date Completed: 10/21/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""
#import file
import emp

def main():

    valid_employee = False

    # loop for validation
    while not valid_employee:

        # get values
        name = input("Enter employee's Name: ")
        id_number = input("Enter employee's ID number: ")
        shift_number = input("Enter the employee's shift number (1:Day, 2:Night): ")
        pay_rate = input("Enter employee's hourly pay rate: ")

        # try block the shift number error won't throw under these circumstances, I just wanted to do it
        try:
            if shift_number == "1" or shift_number == "2":
                worker = emp.ProductionWorker(name, id_number, shift_number, pay_rate)
                valid_employee = True
            else:
                print()
                print("Invalid shift entry, please try again")
                print()
        # catch the error that in this case won't be thrown
        except ValueError as e:
            print("The following error occurred: "+ e)

    #print values
    print()
    print("Production worker information:")
    print("Name: " + worker.get_employee_name())
    print("ID number: " + worker.get_employee_number())
    print("Shift: " + worker.get_shift_number())
    print("Hourly Pay Rate: " + worker.get_hourly_pay_rate())
    print()

main()

    
