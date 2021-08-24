

def print_squares_and_cubes(starting_number, ending_number):
    print("Number\tSquared\tCubed")
    print("------\t-------\t-----")

    for num in range(starting_number, ending_number+1):
        print(str(num) + "\t" + str(num**2) + "\t" + str(num**3))

def get_input(text):
    return int(input(text + ": "))

starting_number = 1
ending_number = 0

while starting_number > ending_number:
    if starting_number != 1 and ending_number != 0 :
        print("Starting number must be less than ending number, please input again")

    starting_number = int(input("Enter starting number: "))
    ending_number = int(input("Enter ending number: "))

print_squares_and_cubes(starting_number, ending_number)