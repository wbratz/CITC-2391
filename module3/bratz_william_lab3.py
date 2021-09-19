"""
Programmer: William Bratz
Assignment: Module 3 - Lab
Date Completed: 9/12/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

# Fuction to write numbers to a file to minimize repeated code
def write_numbers_to_file(numbers, file_name):
    number_file = open(file_name+".txt", "w")
    number_file.write(numbers)
    number_file.close()

# try block to make sure file name is found when reading
try:
    num_list = open("mod3numlist.txt", "r")

    even_nums = ""
    odd_nums = ""

    # Loops through list of numbers from file to split into even and odd
    for num in num_list:
        if int(num) % 2 == 0:
            even_nums += num.rstrip("\n") + "\n"
        else:
            odd_nums += num.rstrip("\n") + "\n"

    write_numbers_to_file(even_nums, "evenNumList")
    write_numbers_to_file(odd_nums, "oddNumList")
except FileNotFoundError:
    print("File could not be found")


