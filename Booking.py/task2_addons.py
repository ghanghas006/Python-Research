#defining the fuction
def select_tickets_and_addons():
    options = []
    total_cost = 0
    
    #asking about the ticket type 
    print("\nTICKET TYPES & ADD_ONS")
    while True:
        #input method
        name = input("Enter ticket type/add-on (e.g., VIP, Standard, Lightstick, Album) or 'done' to finish: ")
        if name.lower() == 'done':
            break
        #price for ticket
        try:
            price = float(input(f"Enter the price for '{name}': $"))
            options.append((name, price))
            total_cost += price
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
        return options, total_cost
    
def main():
    select_tickets_and_addons()

if __name__ == "__main__":
    main()
