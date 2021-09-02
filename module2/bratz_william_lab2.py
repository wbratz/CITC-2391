import random

def display_title():
    print("Dice Roller!")

def roll():
    return random.randint(1, 6)

def roll_dice():
    roll1 = roll()
    roll2 = roll()
    
    print("Die 1:", roll1)
    print("Die 2:", roll2)

    rollValue = roll1+roll2

    print("Total", rollValue)
    print(findNamedResult(roll1, roll2))

def findNamedResult(val1, val2):
    if val1 == 1 and val2 == 1:
        return "Snake Eyes!\n"
    if val1 == 2 and val2 == 2:
        return "Ballerina!\n"
    if val1 == 3 and val2 == 3:
        return "Threes company!\n"
    if val1 == 4 and val2 == 4:
        return "Square Pair!\n"
    if val1 == 5 and val2 == 5:
        return "Five guys burgers and fries?\n"
    if val1 == 6 and val2 == 6:
        return "Boxcars!\n"
    if (val1 == 2 and val2 == 3) or (val1 == 3 and val2 == 2):
        return "Full House!\n"
    if val2 == val1 + 1:
        return "Straight!\n"

    return ""

def main():
    display_title()
    inprogress = input("Roll the dice? (y/n): ").lower()

    while inprogress == "y":
        roll_dice()
        inprogress = input("Roll again? (y/n): ").lower()

    print("Bye!")

main()
