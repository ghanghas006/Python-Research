"""
Title: Requisition System for creating the each requisition with their details.
Author: Roshi
"""
class RequisitionSystem:

    # Colours for the designing codes
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BGYELLOW = "\033[43m"
    LIGHTYELLOW = "\033[93m"
    LIGHTCYAN = "\033[96m"
    LIGHTRED = "\033[91m"
    RESET = "\033[0m"

    # method or variables for the data
    def __init__(self):
        self.total_requisition = 0
        self.approved_requisition = 0
        self.not_approved_requisition = 0
        self.pending_requisition = 0
        self.total_cost = 0
        self.requisition_id = 10000
        self.staff_list = []
        self.status_list = []

    #  method to input the data of the staff
    def staff_info(self):
        print("\nEnter the Staff Information:")
        date = input("Enter the date:")
        staff_id = input("Enter the staff id:")
        staff_name = input("Enter your name: ")
        self.requisition_id += 1
        self.total_requisition += 1

        staff = {
            "date": date,
            "staff_id": staff_id,
            "staff_name": staff_name,
            "requisition_id": self.requisition_id
        }
        self.staff_list.append(staff)

        # printing the staff information
        print(f"\n{RequisitionSystem.GREEN}=================Staff Information:================={RequisitionSystem.RESET}")
        print(f"Date: {date}")
        print(f"Staff ID: {staff_id}")
        print(f"Staff Name: {staff_name}")
        print(f"Requisition ID: {self.requisition_id}\n")

    #  input the data of the requisition items detail and their cost
    def requisitions_details(self):
        total_cost = 0

        print("List of Requisition Items:")
        while True:
            items = input("Enter the requisition items that you want (e.g., Tea) or 'done' to end:")
            if items.lower() == 'done':
                break
            try:
                price = int(input(f"Enter the price for '{items}': $"))
                total_cost += price
            except ValueError:
                print("Invalid price. Please enter a numeric value.")

        self.total_cost = total_cost
        if self.staff_list:
            self.staff_list[-1]["total_cost"] = total_cost
        print(f"Total Cost: ${total_cost}")


    # requisition approval for each requisition
    def requisition_approval(self):
        if 0 < self.total_cost < 500:
            status = "Approved"
            self.approved_requisition += 1
            staff = self.staff_list[-1]
            ref_number = f"{staff['staff_id'][:3].upper()}" + str(self.requisition_id)[-3:]

        else:
            status = "Pending"
            self.pending_requisition += 1
            ref_number = "Not Available"

        
        status_list = {
            "ref_number": ref_number,
            "availability_status": status,
            "requisition_id": self.requisition_id
        }
        self.status_list.append(status_list)
        print(f"Status : {status}")
        print(f"Approval Reference Number: {ref_number}")

    #  manager have to respond the requisitions
    def respond_requisition(self):
        requisition_update = int(input("Enter the number of the requisition to update: "))
        new_availability_status = input("Enter requisition is approved or not approved and still pendings :")

        for status in self.status_list:
            if status['requisition_id'] == requisition_update and status["availability_status"] == "Pending":
                if new_availability_status.lower() == "approved":
                    self.approved_requisition += 1
                    self.pending_requisition -= 1
                    status["availability_status"] = "Approved"
                    for staff in self.staff_list:
                        if staff['requisition_id'] == requisition_update:
                            status["ref_number"] = f"{staff['staff_id'][:3].upper()}" + str(staff['requisition_id'])[-3:].upper()

                elif new_availability_status.lower() == "not approved":
                    self.not_approved_requisition += 1
                    self.pending_requisition -= 1
                    status["availability_status"] = "Not Approved"
                    status["ref_number"] = "Not Available"
                

                print(f"Update Status : {status['availability_status']}")
                print(f"Approval Reference Number: {status['ref_number']}")
                return

    # printing the all requisition details 
    def display_requisition(self):
        print(f"\n{RequisitionSystem.BLUE}===================Display the Requisition:==================={RequisitionSystem.RESET}")
        for staff in self.staff_list:
            print(f"Staff ID: {staff['staff_id']}")
            print(f"Staff Name: {staff['staff_name']}")
            print(f"Requisition ID: {staff['requisition_id']}")
            print(f"Total Cost: ${staff.get('total_cost', 0)}")
            new_status = next((status for status in self.status_list if status.get('requisition_id') == staff['requisition_id']), None)
            if new_status:
                print(f"Status: {new_status['availability_status']}")
                print(f"Approval Reference Number: {new_status['ref_number']}\n")
            else:
                print("Status: Not found.")
                print("Approval Reference Number: N/A.")
                
                

    # printing the each requisition statistics
    def requisition_statistic(self):
        print("Statistics:")
        print(f"The total number of requisition submitted: {self.total_requisition}")
        print(f"The total number of approved requisitions: {self.approved_requisition}")
        print(f"The total number of pending requisition: {self.pending_requisition}")
        print(f"The total number of not approved requisition: {self.not_approved_requisition}")

    # main menu for the class
    def main_menu(self):
        while True:
            # choice for the requisition display
            print(f"\n{RequisitionSystem.RED}=============Requisition Details============={RequisitionSystem.RESET}")
            print("1. Staff Information.")
            print("2. Requisition Details.")
            print("3. Requisition Approval.")
            print("4. Respond Requisitions.")
            print("5. Display Requisition.")
            print("6. Printing the statistics.")
            print("0. Exit.")
            choice = input("Enter your choice(0-6):")
            
            if choice == "1":
                self.staff_info()

            elif choice == "2":
                self.requisitions_details()

            elif choice == "3":
                self.requisition_approval()

            elif choice == "4":
                self.respond_requisition()

            elif choice == "5":
                self.display_requisition()

            elif choice == "6":
                self.requisition_statistic()

            elif choice == "0":
                print("Exiting the Requisition System.")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 6.")


if __name__ == "__main__":
    requisition_system = RequisitionSystem()
    requisition_system.main_menu()
