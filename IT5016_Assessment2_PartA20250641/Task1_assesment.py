"""
Collecting the information about the staff members.
Author: Roshi
"""

# import the staff information
def staff_info(unique_id):
    requisition_id = unique_id 
    unique_id += 1
    
    # input the staff data
    date = input("Enter today's date (DD/MM/YYYY):")
    staff_id = input("Enter your staff id: ")
    staff_name = input("Enter your name: ")

    # printing the all information of the staff
    print("\nPrinting Staff Information:")
    print(f"Date: {date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Requisition ID: {requisition_id}")

    return requisition_id, staff_id, staff_name, date

















