class Member:
    #constructor
    def __init__(self):
        self.total_members = 0
        self.diploma_count = 0
        self.bachelor_count = 0
        self.withdrawn_count = 0
        self.member_list = []

    def register_member(self):
        """
        Register a new member and updates the member list and the statistics.
        """
        print("\nEnter Member Information:")
        student_id = input("Student ID:")
        last_name = input("Last Name:")
        programme = input("Programme (Diploma/Bachelor):")

        self.total_members +=1
        membership_id = self.total_members

        # Track programme count
        if programme.lower() == "diploma":
            self.diploma_count +=1
        elif programme.lower() == "bachelor":
            self.bachelor_count +=1
        else:
            print("Invalid input. Please choose the right programme.")

        member = {
            "membership_id": membership_id,
            "student_id": student_id,
            "last_name": last_name, 
            "programme": programme
        }
        self.member_list.append(member)
        print("Member registered successfully!")

    def withdraw_member(self):
        """
        Withdraws a member and updates the member list and statistics.
        """
        print("\nWithdraw a Member:")
        membership_id = int(input("Enter Membership Id:"))
        last_name = input("Enter Last Name:")

        for member in self.member_list:
            if member["membership_id"] == membership_id and member["last_name"].lower() == last_name.lower():
                self.member_list.remove(member)
                self.withdrawn_count +=1
                self.total_members -=1

                # Adjust programme count
                if member["programme"].lower() == "diploma":
                    self.diploma_count -=1
                elif member["programme"].lower() == "bachelor":
                    self.bachelor_count -=1

                #f-string is used
                print(f"Membership ID: {membership_id} has been withdrawn.")
                return
        print("Member not found or incorrect details provided.")

    def display_members(self):
        """
        Display all members and statistics.
        """
        print("\nRegistered Members:")
        for member in self.member_list:
            #f-string is used
            print(f"Membership ID: {member['membership_id']}")
            print(f"Stident ID: {member['student_id']}")
            print(f"Last Name: {member['last_name']}")
            print(f"Programme: {member['programme']}\n")

        print("Statistics:")
        #f-string is used
        print(f"Total Registered Members: {self.total_members}")
        print(f"Diploma Students: {self.diploma_count}")
        print(f"Bachelor Students: {self.bachelor_count}")
        print(f"Withdrawn Members: {self.withdrawn_count}\n")

    def show_member_details(self):
        """
        Displays details of a specific member by membership ID.
        """
        print("\n Show Members Details:")
        membership_id = int(input("Enter Membership ID:"))

        for member in self.member_list:
            if member["membership_id"] == membership_id:
                #f-string is used
                print(f"Membership ID: {member['membership_id']}")
                print(f"Stident ID: {member['student_id']}")
                print(f"Last Name: {member['last_name']}")
                print(f"Programme: {member['programme']}\n")
                return
        print("Member not found with that membership id.\n")


    def main_menu(self):
        """
        Displays the main menu and handle user choices.
        """

        while True:
            print("\n======Membership Registeration==========")
            print("1. Register a new member")
            print("2. Withdraw a member.")
            print("3. Display all members and statistics.")
            print("4. Show specific Member Details.")
            print("0. Quit.")
            #input method is used
            choice = input("Enter your choice(0-4):")

            if choice == "1":
                self.register_member()
            elif choice == "2":
                self.withdraw_member()
            elif choice == "3":
                self.display_members()
            elif choice == "4":
                self.show_member_details()
            elif choice == "0":
                print("Exiting the Membership System....")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 4.")

# run the program
if __name__ == "__main__":
    member_system = Member()
    member_system.main_menu()
