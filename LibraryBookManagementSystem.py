class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    book = Book(title, author, year)
    books.append(book)
    print(f"\n✅ '{title}' has been added to the library!\n")

def remove_book():
    title = input("Enter book title to remove: ")
    for book in books:
        if book.title.lower() == title.lower():
            books.remove(book)
            print(f"\n❌ '{title}' has been removed from the library.\n")
            return
    print("\n⚠️ Book not found!\n")

def search_book():
    title = input("Enter book title to search: ")
    for book in books:
        if title.lower() in book.title.lower():
            print(f"\n🔍 Found: {book}\n")
            return
    print("\n⚠️ Book not found!\n")

def display_books():
    if not books:
        print("\n📂 No books in the library.\n")
    else:
        print("\n📚 Library Collection:")
        for book in books:
            print(f"- {book}")
        print()

while True:
    print("\n📖 Library Menu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Show All Books")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        remove_book()
    elif choice == '3':
        search_book()
    elif choice == '4':
        display_books()
    elif choice == '5':
        print("\n👋 Exiting Library System. Goodbye!\n")
        break
    else:
        print("\n⚠️ Invalid choice. Please try again.\n")
