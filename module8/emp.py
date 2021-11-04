"""
Programmer: William Bratz
Assignment: Module 8 - Assign
Date Completed: 10/17/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

class Employee:

    #initialize properties
    def __init__(self, name, id_number, department, job_title):
        self._name = name
        self._id_number = id_number
        self._department = department
        self._job_title = job_title

    #return formatted object
    def __str__(self):
        return "Name: " + self._name +"\n"+"ID Number: " + self._id_number +"\n"+"Department: " + self._department +"\n"+"Title: " + self._job_title

    #name setter
    def set_name(self, val):
        self._name = val

    #id setter
    def set_id_number(self, val):
        self._id_number = val

    #department setter
    def set_department(self, val):
        self._department = val

    #job title setter
    def set_job_title(self, val):
        self._job_title = val

    #name getter
    def get_name(self):
        return self._name

    #id getter
    def get_id_number(self):
        return self._id_number

    #department getter
    def get_department(self):
        return self._department

    #job title getter
    def get_job_title(self):
        return self._job_title
