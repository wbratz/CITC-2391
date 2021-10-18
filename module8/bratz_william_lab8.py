"""
Programmer: William Bratz
Assignment: Module 8 - Lab
Date Completed: 10/17/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

class Pet:
    def __init(self, name, animal_type, age):
        self._name = name
        self._animal_type = animal_type
        self._age = age

    #name setter method
    def set_name(self, val):
        self._name = val

    #animal type setter
    def set_animal_type(self, val):
        self._animal_type = val

    #name setter
    def set_age(self, val):
        self._age = val

    #name getter
    def get_name(self):
        return self._name

    #animal type getter
    def get_animal_type(self):
        return self._animal_type

    #age getter
    def get_age(self):
        return self._age

def main():
    cont = True
    pets = []

    while cont:
        pet = Pet()
        pet.set_name(input("Enter the name of your pet: "))
        pet.set_animal_type(input("Enter the type of animal you have: "))
        pet.set_age(input("Enter your pets age: "))

        pets.append(pet)

        again = input("Would you like to add another (y/n)? ").lower()
        if again != "y":
            cont = False

    print()
    print("You have " + str(len(pets)) + " pets!")
    print()
    print("Your pets are")
    for pet in pets:
        print("A " + pet.get_animal_type() + ", named " + pet.get_name() + " who is age " + pet.get_age())

main()
            

