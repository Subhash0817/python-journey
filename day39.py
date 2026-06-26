import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT
)
""")

class Library:

    def add_book(self, title, author):
        cursor.execute(
            "INSERT INTO books(title, author) VALUES (?, ?)",
            (title, author)
        )
        conn.commit()
        print("Book Added Successfully!")

    def view_books(self):
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        if books:
            for book in books:
                print(book)
        else:
            print("No Books Found")

    def delete_book(self, book_id):
        cursor.execute(
            "DELETE FROM books WHERE id=?",
            (book_id,)
        )
        conn.commit()
        print("Book Deleted Successfully!")

library = Library()

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(title, author)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book_id = int(input("Enter Book ID: "))
        library.delete_book(book_id)

    elif choice == "4":
        break

    else:
        print("Invalid Choice")

conn.close()