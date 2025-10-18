import json
from datetime import datetime, timedelta

# ------------------ Book Class ------------------
class Book:
    def __init__(self, title, author, quantity=1):
        self.title = title
        self.author = author
        self.quantity = quantity  # available copies
        self.borrowed = []  # list of dicts: {"name":..., "due_date":...}

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available Copies: {self.quantity}")
        if self.borrowed:
            print("Borrowed Copies:")
            for b in self.borrowed:
                print(f"  Borrower: {b['name']}, Due Date: {b['due_date']}")
        print("-" * 20)

    def borrow_book(self, borrower_name, days=14):
        if self.quantity > 0:
            self.quantity -= 1
            due_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
            self.borrowed.append({"name": borrower_name, "due_date": due_date})
            print(f"'{self.title}' borrowed by {borrower_name}. Due on {due_date}.")
        else:
            print(f"Sorry, '{self.title}' is not available right now.")

    def return_book(self, borrower_name):
        for b in self.borrowed:
            if b['name'].lower() == borrower_name.lower():
                self.borrowed.remove(b)
                self.quantity += 1
                print(f"{borrower_name} returned '{self.title}'.")
                return
        print(f"No record found for {borrower_name} borrowing '{self.title}'.")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "quantity": self.quantity,
            "borrowed": self.borrowed
        }

    @staticmethod
    def from_dict(data):
        book = Book(data["title"], data["author"], data["quantity"])
        book.borrowed = data.get("borrowed", [])
        return book

# ------------------ File Handling ------------------
FILENAME = "library.json"

def save_library(library):
    with open(FILENAME, "w") as f:
        json.dump([book.to_dict() for book in library], f)
    print("Library saved successfully.")

def load_library():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            return [Book.from_dict(book) for book in data]
    except FileNotFoundError:
        return []

# ------------------ Library Functions ------------------
library = load_library()

def display_all_books():
    if not library:
        print("Library is empty.")
        return
    print("\nLibrary Books:")
    for book in library:
        book.display_details()

def find_book_by_title(title):
    for book in library:
        if book.title.lower() == title.lower():
            return book
    return None

def search_books():
    query = input("Enter title or author to search: ").lower()
    results = [book for book in library if query in book.title.lower() or query in book.author.lower()]
    if results:
        print(f"\nSearch Results ({len(results)} found):")
        for book in results:
            book.display_details()
    else:
        print("No books matched your search.")

def borrow_book():
    title = input("Enter the title of the book you want to borrow: ")
    book = find_book_by_title(title)
    if book:
        borrower = input("Enter your name: ")
        try:
            days = int(input("Enter number of days to borrow (default 14): ") or 14)
        except ValueError:
            days = 14
        book.borrow_book(borrower, days)
        save_library(library)
    else:
        print(f"'{title}' not found in the library.")

def return_book():
    title = input("Enter the title of the book you want to return: ")
    book = find_book_by_title(title)
    if book:
        borrower = input("Enter your name: ")
        book.return_book(borrower)
        save_library(library)
    else:
        print(f"'{title}' not found in the library.")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    try:
        quantity = int(input("Enter number of copies: "))
    except ValueError:
        print("Invalid input. Setting quantity to 1.")
        quantity = 1
    existing_book = find_book_by_title(title)
    if existing_book and existing_book.author.lower() == author.lower():
        existing_book.quantity += quantity
        print(f"Added {quantity} more copies of '{title}'. Total copies: {existing_book.quantity}")
    else:
        library.append(Book(title, author, quantity))
        print(f"Book '{title}' by {author} added with {quantity} copies.")
    save_library(library)

# ------------------ Menu ------------------
def menu():
    while True:
        print("\n--- Library Menu ---")
        print("1. Display all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add a new book / copies")
        print("5. Search books")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_all_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            add_book()
        elif choice == "5":
            search_books()
        elif choice == "6":
            print("Exiting library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

# ------------------ Start Program ------------------
menu()
