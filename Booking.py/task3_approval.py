#defining the function
def approve_booking(total_cost, ticket_id, id_number):
    # if and else statement is used
    status = "Confirmed" if total_cost > 0 else "Pending"
    ref_number = id_number[:3].upper() + str(ticket_id)[-2:]
    return status, ref_number
