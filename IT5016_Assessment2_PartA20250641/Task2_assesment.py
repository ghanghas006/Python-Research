"""
Total amount of the Requisition Items
Author: Roshi
"""

# import staff info from Task1
from Task1_assesment import staff_info

# defining function for the requisition total
def requisition_total():
    options = []
    total_cost = 0

    # printing the requisition items
    print("\n Requestition Items")
    while True:
        #input method is usef
        items = input("Enter the requisition items that you want (e.g., Tea) or 'done' to finish: ")
        if items.lower() == 'done':
            break
        try:
            price = int(input(f"Enter the price for '{items}': $"))
            options.append((items, price))
            total_cost += price
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
    return options, total_cost
