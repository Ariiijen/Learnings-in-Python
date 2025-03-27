import tkinter as tk
from tkinter import messagebox, scrolledtext

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class LibraryApp:
    def __init__(self, root):
        self.books = []
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f4f8")  # Light blue-gray background

        # Styling constants
        self.BG_COLOR = "#f0f4f8"
        self.BUTTON_COLOR = "#FFB8E0"  # Blue
        self.BUTTON_HOVER = "#FFCFEF"  # Darker blue
        self.TEXT_COLOR = "#000000"    # Dark gray
        self.ACCENT_COLOR = "#0A5EB0"  # Red accent

        # Create main frame
        self.main_frame = tk.Frame(root, bg=self.BG_COLOR)
        self.main_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Title label
        tk.Label(self.main_frame, text="📚 Library Management System", 
                font=("Helvetica", 20, "bold"), 
                bg=self.BG_COLOR, 
                fg=self.TEXT_COLOR).pack(pady=10)

        # Buttons frame
        self.button_frame = tk.Frame(self.main_frame, bg=self.BG_COLOR)
        self.button_frame.pack(pady=10)

        # Button style function
        def create_styled_button(text, command):
            btn = tk.Button(self.button_frame, text=text, command=command,
                          bg=self.BUTTON_COLOR, fg="white",
                          font=("Helvetica", 10, "bold"),
                          relief="flat", padx=10, pady=5)
            btn.pack(side=tk.LEFT, padx=5)
            btn.bind("<Enter>", lambda e: btn.config(bg=self.BUTTON_HOVER))
            btn.bind("<Leave>", lambda e: btn.config(bg=self.BUTTON_COLOR))
            return btn

        # Create buttons
        create_styled_button("Add Book", self.add_book_window)
        create_styled_button("Remove Book", self.remove_book_window)
        create_styled_button("Search Book", self.search_book_window)
        create_styled_button("Show All Books", self.display_books)
        create_styled_button("Exit", root.quit)

        # Output area
        self.output_text = scrolledtext.ScrolledText(self.main_frame, 
                                                   height=15, 
                                                   width=70,
                                                   bg="white",
                                                   fg=self.TEXT_COLOR,
                                                   font=("Helvetica", 10),
                                                   borderwidth=2,
                                                   relief="groove")
        self.output_text.pack(pady=10, fill="both", expand=True)

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    def style_window(self, window, title):
        window.configure(bg=self.BG_COLOR)
        tk.Label(window, text=title, 
                font=("Helvetica", 12, "bold"), 
                bg=self.BG_COLOR, 
                fg=self.TEXT_COLOR).pack(pady=10)

    def create_entry(self, window, label_text):
        tk.Label(window, text=label_text, 
                bg=self.BG_COLOR, 
                fg=self.TEXT_COLOR).pack(pady=5)
        entry = tk.Entry(window, width=30, 
                        bg="white", 
                        fg=self.TEXT_COLOR,
                        relief="flat",
                        borderwidth=2)
        entry.pack()
        return entry

    def create_submit_button(self, window, command):
        btn = tk.Button(window, text="Submit", 
                       command=command,
                       bg=self.ACCENT_COLOR, 
                       fg="white",
                       font=("Helvetica", 10, "bold"),
                       relief="flat", padx=10, pady=5)
        btn.pack(pady=15)
        btn.bind("<Enter>", lambda e: btn.config(bg="#c0392b"))
        btn.bind("<Leave>", lambda e: btn.config(bg=self.ACCENT_COLOR))
        return btn

    def add_book_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Book")
        add_window.geometry("300x250")
        self.style_window(add_window, "Add New Book")

        title_entry = self.create_entry(add_window, "Title:")
        author_entry = self.create_entry(add_window, "Author:")
        year_entry = self.create_entry(add_window, "Year:")

        def submit_book():
            title, author, year = title_entry.get(), author_entry.get(), year_entry.get()
            if title and author and year:
                book = Book(title, author, year)
                self.books.append(book)
                self.clear_output()
                self.output_text.insert(tk.END, f"✅ '{title}' has been added to the library!\n")
                add_window.destroy()
            else:
                messagebox.showwarning("Warning", "Please fill all fields!")

        self.create_submit_button(add_window, submit_book)

    def remove_book_window(self):
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Book")
        remove_window.geometry("300x150")
        self.style_window(remove_window, "Remove Book")

        title_entry = self.create_entry(remove_window, "Enter book title to remove:")

        def remove():
            title = title_entry.get()
            for book in self.books:
                if book.title.lower() == title.lower():
                    self.books.remove(book)
                    self.clear_output()
                    self.output_text.insert(tk.END, f"❌ '{title}' has been removed from the library.\n")
                    remove_window.destroy()
                    return
            self.clear_output()
            self.output_text.insert(tk.END, "⚠️ Book not found!\n")
            remove_window.destroy()

        self.create_submit_button(remove_window, remove)

    def search_book_window(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Book")
        search_window.geometry("300x150")
        self.style_window(search_window, "Search Book")

        title_entry = self.create_entry(search_window, "Enter book title to search:")

        def search():
            title = title_entry.get()
            for book in self.books:
                if title.lower() in book.title.lower():
                    self.clear_output()
                    self.output_text.insert(tk.END, f"🔍 Found: {book}\n")
                    search_window.destroy()
                    return
            self.clear_output()
            self.output_text.insert(tk.END, "⚠️ Book not found!\n")
            search_window.destroy()

        self.create_submit_button(search_window, search)

    def display_books(self):
        self.clear_output()
        if not self.books:
            self.output_text.insert(tk.END, "📂 No books in the library.\n")
        else:
            self.output_text.insert(tk.END, "📚 Library Collection:\n")
            for book in self.books:
                self.output_text.insert(tk.END, f"- {book}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()