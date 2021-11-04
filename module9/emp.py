"""
Programmer: William Bratz
Assignment: Module 9 - Lab
Date Completed: 10/21/21
Course: CITC 2391 - C01
Instructor: Martin Bell
""" 

class Employee:

    # Constructor
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

    # set employee name
    def set_employee_name(self, value):
        self.employee_name = value

    # set employee number
    def set_employee_number(self, value):
        self.employee_number = value

    # get employee_name
    def get_employee_name(self):
        return self.employee_name

    # get employee_number
    def get_employee_number(self):
        return self.employee_number

# producction worker class that inherits from employee
class ProductionWorker(Employee):

    #constructor, passes values to base class
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        Employee.__init__(self, employee_name, employee_number)        
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    # shit number setter
    def set_shift_number(self, value):
        if value == "1" or value == "2":
            self.shift_number = value
        else:
            raise ValueError("An invalid shift was entered.")

    # hourly pay setter
    def set_hourly_pay_rate(self, value):
        self.hourly_pay_rate = value

    # shift number getter
    def get_shift_number(self):
        return self.shift_number

    # hourly pay getter
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

class Shiftsupervisor(Employee):

    #constructor
    def __init__(self, employee_name, employee_number, annual_salary, annual_bonus):
        super().__init__(employee_name, employee_number)
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus

    # set annual_salary
    def set_annual_salary(self, val):
        self.annual_salary = val

    # set bonus
    def set_annual_bonus(self, val):
        self.annual_bonus = val

    # salary_getter
    def get_annual_salary(self):
        return self.annual_salary

    # bonus getter
    def get_annual_bonus(self):
        return self.annual_bonus

