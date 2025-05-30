def concert_booking(id_counter):
    #collecting the fans's information during the ticket booking for band tour
    print("BAND TOUR TICKET BOOKING")
    fan_id = input("Enter your form of ID (Passport or Driver's License'):" )
    id_number = input("Enter your ID number:")
    fan_name = input("Enter your name:")
    tour_city = input("Which city would like to attend the concert in?: ")

    ticket_id = id_counter +1
    id_counter = ticket_id

    return id_counter, ticket_id, id_number, fan_id, fan_name, tour_city

concert_booking(id_counter)

