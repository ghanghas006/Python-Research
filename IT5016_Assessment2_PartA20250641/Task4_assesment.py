"""
Display the all basic information related to the Requisition of the staff.
Author: Roshi
"""

# importing the information from the last tasks
from Task1_assesment import staff_info
from Task2_assesment import requisition_total
from Task3_assesment import requisition_approval

# import display requisition function
def display_requisitions():
    unique_id = 10000
    unique_id += 1
    
# functions from the last tasks
    requisition_id, staff_id, staff_name, date = staff_info(unique_id)
    options, total_cost = requisition_total()
    status, ref_number = requisition_approval(total_cost, staff_id, requisition_id)

# printing all the information
    print("\n Printing Requisitions:")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total cost: ${total_cost}")
    print(f"Status: {status}")
    print(f"Approval Reference Number : {ref_number}")

def main():
        display_requisitions()

if __name__ == "__main__":
    main()