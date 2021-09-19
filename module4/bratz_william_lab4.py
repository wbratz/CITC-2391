"""
Programmer: William Bratz
Assignment: Module 4 - Lab
Date Completed: 9/18/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

def main():
    display_greeting()
    quarterly_sales = get_quarterly_sales()

    print()
    process_sales(quarterly_sales)


def display_greeting():
    print("The Quarterly Sales program\n")

def get_quarterly_sales():
    # put this in a tuple because we need to get the values for each quarter but we don't want to be able to edit the values
    sales_quarters = ("Q1", "Q2", "Q3", "Q4")
    salesList = []
    
    # Loop through quarters to get the input for each and add to a list
    for quarter in sales_quarters:
        userInput = input("Enter sales for " + quarter + ": ")
        salesList.append(int(userInput))

    return salesList

def process_sales(salesData):
    # I split each of the calculations into separate functions
    average_sales = get_average(salesData)
    total_sales = get_total(salesData)
    min_sales = get_min(salesData)
    max_sales = get_max(salesData)

    #print the results from the function calls
    print("Total: $" + str(total_sales))
    print("Average Quater: $" + str(average_sales))
    print("Lowest Quarter: $" + str(min_sales))
    print("Highest Quarter: $" + str(max_sales))

    
def get_average(salesData):

    #to get the average all we need to do is get the total and divide it by the length of our list
    total = get_total(salesData)

    return total / len(salesData)

def get_total(salesData):
    total_sales = 0

    # pretty straight forward, loop through the data and add to the total
    for data in salesData:
        total_sales += data

    return float(total_sales)

def get_min(salesData):
    # this is interesting because python doesn't have a max value for ints
    # in C# i'd do something like int.maxvalue but python3 doesn't recognize a limit to the value placed in an integer 
    # so technically this code is flawed in that if the company does over 100 billion dollars in sales each quarter then it won't work
    # a better approach would be to initialize min as like -1 and then set a condition if min_sale = -1 then set min_sale to whatever value
    # an even better approach would be to initialize min_sale as salesdata[0]... I'm actually going to comment this out and do that..
    
    #min_sale = -1 
    min_sale = salesData[0]

    for data in salesData:
        if data < min_sale:
            min_sale = data
    return float(min_sale)

def get_max(salesData):
    # same idea as min sale
    # start with a low number, sales can't be lower than 0 then compare each value in a loop until you get the highest number
    max_sale = 0

    for data in salesData:
        if data > max_sale:
            max_sale = data

    return float(max_sale)

main()
