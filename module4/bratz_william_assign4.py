"""
Programmer: William Bratz
Assignment: Module 6 - Lab
Date Completed: 9/24/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""


def read_data():
    data_list = []
    file_data = open("nutrition_data.csv", "r")

    while file_data.readline() != "":
        line_data = file_data.readline().rstrip("\n")
        line_items = line_data.split(",")
        data_list.append(line_items)

    file_data.close()

    return data_list


def create_separate_list(main_list, user_choice):
    fruit_list = []
    vegetable_list = []
    protien_list = []
    grains_list = []
    dairy_list = []

    for list in main_list:
        if(list[0] == "Dairy"):
                dairy_list.append(list[1:4])
        elif(list[0] == "Meat"):
                protien_list.append(list[1:4])
        elif(list[0] == "Vegetables"):
                vegetable_list.append(list[1:4])
        elif(list[0] == "Fruit"):
                fruit_list.append(list[1:4])
        elif(list[0] == "Grains"):
                grains_list.append(list[1:4])
    
    if(user_choice == 4):
        return fruit_list
    elif(user_choice == 1):
        return dairy_list
    elif(user_choice == 2):
        return protien_list
    elif(user_choice == 3):
        return vegetable_list
    elif(user_choice == 5):
        return grains_list


def display_menu():
    print("1. Dairy")
    print("2. Meat")
    print("3. Vegetables")
    print("4. Fruit")
    print("5. Grains")


def main():
    data = read_data()
    user_selected = False

    print("Nutrition by Food Group")

    while not user_selected:
        display_menu()
        print()
        user_choice = int(input("Enter your food group choice: (1-5): "))
        print()

        if(user_choice >= 1 and user_choice <= 5):
            user_list = create_separate_list(data, user_choice)

            print("Name\t\t\tAmount\t\tCalories")
            print("----------------------------------------------------")
            for item in user_list:
                print("{: <23} {: <15} {: <20}".format(*item))

            print()

            user_continue = input("Would you like to continue? ").lower()
            if(user_continue == 'n'):
                user_selected = True
        else:
            print("invalid selection, try again")
            print()

main()

        

    
    