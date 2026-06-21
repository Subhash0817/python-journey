class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:

    def __init__(self):
        self.books = []

    def add_book(self):

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(title, author)

        self.books.append(book)

        print("Book Added Successfully")

    def view_books(self):

        if not self.books:
            print("No Books Available")
            return

        for book in self.books:

            status = "Available" if book.available else "Issued"

            print(
                f"Title: {book.title} | "
                f"Author: {book.author} | "
                f"Status: {status}"
            )

    def issue_book(self):

        title = input("Enter Book Title: ")

        for book in self.books:

            if book.title == title and book.available:

                book.available = False

                print("Book Issued Successfully")

                return

        print("Book Not Available")

    def return_book(self):

        title = input("Enter Book Title: ")

        for book in self.books:

            if book.title == title:

                book.available = True

                print("Book Returned Successfully")

                return

        print("Book Not Found")


library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.issue_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")