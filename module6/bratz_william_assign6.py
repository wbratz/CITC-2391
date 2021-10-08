"""
Programmer: William Bratz
Assignment: Module 6 - assignment
Date Completed: 9/30/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

import random

# initialize dictionary
dict = {
"Alabama" : "Montgomery",
"Alaska" : "Juneau",
"Arizona" : "Phoenix",
"Arkansas" : "Little Rock",
"California" : "Sacramento",
"Colorado" : "Denver",
"Connecticut" : "Hartford",
"Delaware" : "Dover",
"Florida" : "Tallahassee",
"Georgia" : "Atlanta",
"Hawaii" : "Honolulu",
"Idaho" : "Boise",
"Illinois" : "Springfield",
"Indiana" : "Indianapolis",
"Iowa" : "Des Moines",
"Kansas" : "Topeka",
"Kentucky" : "Frankfort",
"Louisiana" : "Baton Rouge",
"Maine" : "Augusta",
"Maryland" : "Annapolis",
"Massachusetts" : "Boston",
"Michigan" : "Lansing",
"Minnesota" : "Saint Paul",
"Mississippi" : "Jackson",
"Missouri" : "Jefferson City",
"Montana" : "Helena",
"Nebraska" : "Lincoln",
"Nevada" : "Carson City",
"New Hampshire" : "Concord",
"New Jersey" : "Trenton",
"New Mexico" : "Santa Fe",
"New York" : "Albany",
"North Carolina" : "Raleigh",
"North Dakota" : "Bismarck",
"Ohio" : "Columbus",
"Oklahoma" : "Oklahoma City",
"Oregon" : "Salem",
"Pennsylvania" : "Harrisburg",
"Rhode Island" : "Providence",
"South Carolina" : "Columbia",
"South Dakota" : "Pierre",
"Tennessee" : "Nashville",
"Texas" : "Austin",
"Utah" : "Salt Lake City",
"Vermont" : "Montpelier",
"Virginia" : "Richmond",
"Washington" : "Olympia",
"West Virginia" : "Charleston",
"Wisconsin" : "Madison",
"Wyoming" : "Cheyenne"
}

# gets new state to not repeat code
def get_new_state():
    return random.choice(list(dict.keys()))

# gets new city to not repeat code
def get_city(state):
    return dict.get(state)

# initalizes variables we need
state = get_new_state()
city = get_city(state)
user_continue = True
correct_answers = 0;
incorrect_answers = 0;

# while the user hasn't selected to quit
while user_continue:
    user_answer = input("What is the capital of " + state + "? (or answer 0 to quit): ").lower()
    
    # if the correct answer go down the correct path
    if user_answer == city.lower():
        print("That is correct.\n")
        state = get_new_state()
        city = get_city(state)
        correct_answers += 1
    # if the answer is incorrect go down that path
    elif user_answer != "0":
        print("That is incorrect.\n")
        state = get_new_state()
        city = get_city(state)
        incorrect_answers += 1
    # the only other valid answer is that the user wanted to quit
    else:
        user_continue = False
        
# print results after they quit
print("You had " + str(correct_answers) + " correct responses and " + str(incorrect_answers) + " incorrect responses.")