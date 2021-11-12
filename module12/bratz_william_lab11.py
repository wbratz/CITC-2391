"""
Programmer: William Bratz
Assignment: Module 12 - Lab
Date Completed: 11/11/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

def print_lines(n):    
    print("Recursion " + str(n))
    if n > 1:
        print_lines(n - 1)
    
    ## This is the only way I could figure out how to get the right output inside a for loop after the recursion
    if(n == user_input):
        for i in range(n):
            print("*" * (i + 1), end="\n")

user_input = int(input("How many lines to display? "))

print_lines(user_input)