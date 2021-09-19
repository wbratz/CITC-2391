"""
Programmer: William Bratz
Assignment: Module 3 - assignment
Date Completed: 9/12/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

def display_menu(file_name):
    exit_selected = False

    #while the user has not selected exit, keep displaying the menu
    while not exit_selected:
        print("COMMAND MENU"+"\n"+
        "view - View a contact"+"\n"+
        "add - Add a contact"+"\n"+
        "del - Delete a contact"+"\n"+
        "exit - Exit program\n")

        user_selection = input("Enter a command: ")
        print()
        if user_selection == "view":
            view_contacts(file_name)
        elif user_selection == "add":
            add_contacts(file_name)
        elif user_selection == "del":
            delete_contacts(file_name)
        elif user_selection =="exit":
            print("Good-bye")
            exit_selected = True
        else:
            print("You did not enter a valid selection, please try again\n")

def view_contacts(file_name):
    contact_count = 0
    file = open(file_name, "r")
    
    #print every line in the file with a number in front
    for line in file:
        contact_count += 1
        print(str(contact_count) + ". " + line.rstrip("\n"))
    
    print("")

    file.close()

def add_contacts(file_name):

    #Get user inputs
    name = input("Enter name: ")
    email = input("Enter email address: ")
    phone = input("Enter phone number: ")

    #append the user inputs to the end of the file
    file = open(file_name, "a")
    file.write("\n" + name + ", " + email + ", " + phone)

    file.close()

    print()

def delete_contacts(file_name):
    
    
    view_contacts(file_name)

    #take the user selection of the contact to delete
    to_del = input("Enter contact number to delete: ")

    file = open(file_name, "r")
    
    updated_contents = ""
    contact_count = 0

    #iterate through the file and build up a string of all the values that don't match the user selection
    for line in file:
        contact_count += 1
        if str(contact_count) != to_del:
            updated_contents += line

    file.close()

    #open the file for writing and write the new contents that doesn't contain the deleted line
    file = open(file_name, "w")
    file.write(updated_contents[:-1])
    file.close()        
    
    print("Contact deleted successfully!")
    print()
    

def main():
    success = False
    contact_file_name = ""

    print("Contact Manager")
    print("")

    #as long as the filename is invalid keep asking for it
    while not success:
        try:
            contact_file_name = input("Enter the name of the contact file: ")
            print("")
            contact_file = open(contact_file_name, "r")
            contact_file.close()
            success = True
        except FileNotFoundError:
            print("File not found")
    
    display_menu(contact_file_name)


main() 