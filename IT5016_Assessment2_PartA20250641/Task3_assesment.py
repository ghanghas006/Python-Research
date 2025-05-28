"""
Responding to the requisition requests.
Author: Roshi
"""

# import the functions from Task1, Task2
from Task1_assesment import staff_info
from Task2_assesment import requisition_total

# import the approval function
def requisition_approval(total_cost, staff_id, requisition_id):
    status = "Approved" if total_cost > 0 and total_cost < 500 else "Pending"
    ref_number = staff_id[:3].upper() +str(requisition_id)[-3:]
    return status, ref_number

