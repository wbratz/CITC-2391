"""
Programmer: William Bratz
Assignment: Module 9 - Assignment
Date Completed: 10/21/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

from emp import Shiftsupervisor

def main():
    # get values
    name = input("Enter the name: ")
    id = input("Enter the ID number: ")
    salary = input("Enter the annual salary: ")
    bonus = input("Enter the bonus: ")

    shift_supervisor = Shiftsupervisor(name, id, salary, bonus)

    # output object information
    print("Shift supervisor worker information: ")
    print()
    print("Name: " + shift_supervisor.get_employee_name())
    print("ID number: " + shift_supervisor.get_employee_number())
    # format salary and bonus as money
    print("Annual salary: " + "${:,.2f}".format(float(shift_supervisor.get_annual_salary())))
    print("Annual Production Bonus: " + "${:,.2f}".format(float(shift_supervisor.get_annual_bonus())))

main()