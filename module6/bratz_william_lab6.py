"""
Programmer: William Bratz
Assignment: Module 6 - Lab
Date Completed: 9/29/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

# read the files
first_file = open("FirstFile.txt", "r")
second_file = open("SecondFile.txt", "r")

# create sets from the files
first_file_set = set(first_file.read().lower().replace(".", "").split())
second_file_set = set(second_file.read().lower().replace(".", "").split())

## Print unique words contained in both files
print("Unique words contained in both files: \n" + str(first_file_set.union(second_file_set)) + "\n")

## Print a list of words that appear in both files
print("List of words that appear in both files: \n" + str(first_file_set.intersection(second_file_set)) + "\n")

## Words in the first file, that aren't in the second
print("List of words that appear in the first file, not in the second: \n" + str(first_file_set.difference(second_file_set)) + "\n")

## words in the second file not in the first
print("List of words that appear in the second file, not in the first: \n" + str(second_file_set.difference(first_file_set)) + "\n")

# words that are in the first or second, not in both
print("List of words that appear in either the first or second file, not both: \n" + str(first_file_set.symmetric_difference(second_file_set)) + "\n")

