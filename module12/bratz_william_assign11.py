"""
Programmer: William Bratz
Assignment: Module 12 - Assignment
Date Completed: 11/11/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

## greatest common divisor method
def get_gcd(num1, num2):
    
    ## use modulo to get remainder
    remainder = num1 % num2

    ## if its 0 return it
    if remainder == 0:
        return num2

    ## otherwise return the recursive function call
    return get_gcd(num2, remainder) 

def main():
    user_input = False
    print("Welcome to the GREATEST COMMON DIVISOR!")
    print()
    while not user_input:
        first_number = int(input("Enter number 1: "))
        second_number = int(input("Enter number 2: "))

        if first_number < second_number:
            print("First number must be greater than the second number. Try again.")
            continue

        # print result of recursive function
        print("Greatest common divisor: " + str(get_gcd(first_number, second_number)))
        print()
        cont = input("Continue? (y/n) ").lower()

        if cont != "y":
            user_input = True
            print()
            print("Bye!")

main()