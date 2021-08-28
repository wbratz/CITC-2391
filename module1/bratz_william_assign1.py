cont = True

def calculate_shipping(cost):
    if cost < 30:
        return 5.95
    elif cost <= 49.99:
        return 7.95
    elif cost <= 74.99:
        return 9.95
    else:
        return 0 

print("===============================================================")
print("Shipping Calculator")
print("===============================================================")
print("")

while cont:
    items_cost = -1

    while(items_cost < 0):
        items_cost = float(input("Enter cost of items ordered: "))

        if(items_cost < 0):
            print ("Item cost must be a positive number. Please try again.")
            print("")

            
    print("")
    shipping_cost = calculate_shipping(items_cost)
    print("Shipping cost:", shipping_cost)
    print("Total cost: " + "{:.2f}".format(items_cost + shipping_cost))


    cont_selection = input("Continue? (y/n): ")
    print("")
    print("===============================================================")
    if (cont_selection.lower() != "y"):
        cont = False

print("Bye!")



