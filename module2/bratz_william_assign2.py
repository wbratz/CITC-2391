import conversion

def display_title():
    print("Feet and Meters Converter")

def display_menu():
    print ("\nConversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet\n")

def determine_continue(inpt):
    if inpt == "y":
        return True
    
    return False

def main():
    display_title()

    cont = True

    while cont:
        display_menu()
        user_input = input("Select a conversion (a/b):").lower()

        if user_input == "a":
            val = int(input("Enter feet: "))
            print("\nThe answer is " + str(round(conversion.feet_to_meters(val), 2)) + " meters\n")
        elif user_input == "b":
            val = int(input("Enter meters: "))
            print("\nThe answer is " + str(round(conversion.meters_to_feet(val), 2)) + " feet\n")
        else:
            print("Invalid selection\n")

        continue_input = input("Would you like to perform another conversion (y/n): ").lower()

        cont = determine_continue(continue_input)        

    print("Thanks, Bye!")

main()