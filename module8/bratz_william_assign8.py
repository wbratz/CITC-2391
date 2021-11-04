"""
Programmer: William Bratz
Assignment: Module 8 - Lab
Date Completed: 10/18/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""
#import employee from emp file
from emp import Employee

def main():
    #initialize an array
    employees = []

    #initialize a count for use in the loop
    count = 1

    #append employees to array
    employees.append(Employee("Susan Meyers", "47899", "Accounting", "Vice President"))
    employees.append(Employee("Mark Jones", "39119", "IT", "Programmer"))
    employees.append(Employee("Joy Rogers", "81774", "Manufacturing", "Engineer"))

    #loop through, print count, employee, and increment count
    for employee in employees:
        print("Employee " + str(count) +":")
        print(employee)
        print()
        count+= 1

main()



