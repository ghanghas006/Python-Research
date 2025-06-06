#importing the information from the other tasks
from task1_booking import concert_booking
from task2_addons import select_tickets_and_addons
from task3_approval import approve_booking

#defining the function
def display_concert_booking():
    id_counter = 5000

    #last tasks deatils
    id_counter, ticket_id, id_number, fan_id, fan_name, tour_city = concert_booking(id_counter)
    selected_options, total_cost = select_tickets_and_addons()
    status, ref_number = approve_booking(total_cost, ticket_id,id_number)

    #printing concert 
    
    print("\n YOUR CONCERT BOOKING RECEIPT")
    #formatting string is used here
    print(f"Ticket ID: {ticket_id}")
    print(f"Name: {fan_name}")
    print(f"ID Type: {fan_id}")
    print(f"ID Number: {id_number}")
    print(f"Tour City: {tour_city}")
    print(f"Selected Options:")
    if selected_options:
        for item, price in selected_options:
            print(f" - {item}: ${price}")
    else:
        print("No options selected.")
    print(f"Total cost: ${total_cost}")
    print(f"Booking Status: {status}")
    print(f"Approval Refrence #: {ref_number}")

def main():
    display_concert_booking()

if __name__ == "__main__":
    main()
