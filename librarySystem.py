#parent class
class Book:
    #colors for designing
    RED = "\033[31m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BGYELLOW = "\033[43m"
    LIGHTYELLOW = "\033[93m"
    LIGHTCYAN = "\033[96m"
    LIGHTRED = "\033[91m"
    RESET = "\033[0m"

    #constructor
    def __init__(self, title, author, publication_year, availability_status = True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability_status = availability_status
    #defining the function
    def display_details(self):
        status = f"{Book.GREEN}Available{Book.RESET}" if self.availability_status else f"{Book.LIGHTCYAN}Checked Out{Book.RESET}"
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Publication Year: {self.publication_year}\n"
                f"Status: {status}")
    


#child classes
class Patron:
    #constructor
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []


    def register_book(self, book):
        if book.availability_status:
            self.borrowed_books.append(book)
            book.availability_status = False
            return f"Book '{book.title}' has been borrowed."
        else:
            return f"Book '{book.title}' is currently unavailable."
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.availability_status = True
            return f"Book '{book.title}' has been returned."
        else:
            return f"Book '{book.title}' was not borrowed by this patron."
        

class Library:
    #constructor
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        return f"Book '{Book.LIGHTCYAN}{book.title}{Book.RESET}' has been added to the library."
    
    def register_patron(self, patron):
        self.patrons.append(patron)
        return f"Book '{Book.YELLOW}{patron.name}{Book.RESET}' has been registered."
    
    def display_books(self):
        return "\n".join(book.display_details() for book in self.books)
    
    def find_books(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
            return None
    def find_patron(self, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                return patron
        return None
    
if __name__ == "__main__":
    library = Library()

    while True:
        #f-string is used
        print(f"{Book.BGYELLOW}============Library Management System============{Book.RESET}")
        print(f"1. To {Book.LIGHTCYAN}Add a Book{Book.RESET}, press {Book.BLUE} '1'{Book.RESET}")
        print(f"2. To {Book.LIGHTCYAN}Register a Parton{Book.RESET}, press {Book.BLUE} '2'{Book.RESET}")
        print(f"3. To {Book.LIGHTCYAN}Display Books{Book.RESET}, press {Book.BLUE} '3'{Book.RESET}")
        print(f"4. To {Book.LIGHTCYAN}Borrow a Book{Book.RESET}, press {Book.BLUE} '4'{Book.RESET}")
        print(f"5. To {Book.LIGHTCYAN}Return a Book{Book.RESET}, press {Book.BLUE} '5'{Book.RESET}")
        print(f"6. To {Book.LIGHTCYAN}Exit{Book.RESET}, press {Book.BLUE} '0'{Book.RESET}")

        #input method is used
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_year = int(input("Enter publication year: "))
            book = Book(title, author, publication_year)
            print(library.add_book(book))
        elif choice == "2":
            name = input("Enter patron's name: ")
            patron_id = input("Enter patron's ID: ")
            patron = Patron(name, patron_id)
            print(library.register_patron(patron))
        elif choice == "3":
            print("\nBooks in the Library: ")
            print(library.display_books())
        elif choice == "4":
            patron_id = input("Enter your ID: ")
            title = input("Enter Book title to borrow: ")
            patron = library.find_patron(patron_id)
            book = library.find_books(title)
            if patron and book:
                print(patron.register_book(book))
            else:
                print("Invalid patron ID or Book title.")

        elif choice == "5":
            patron_id = input("Enter your ID: ")
            title = input("Enter book title to return: ")
            patron = library.find_patron(patron_id)
            book = library.find_books(title)
            if patron and book:
                print(patron.return_book(book))
            else:
                print("Invalid patron ID or Book title.")

        elif choice == "0":
            print("Exiting the system.")
            exit()
        else:
            print("Invalid choice. Please try again.")
