import tkinter as tk

# Function to perform calculations
def on_button_click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))  # Evaluate the expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Configure the window size and background color
root.geometry("350x450")
root.config(bg="#f8e1e1")  # Light pink background

# Create the display with a minimalist design
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="flat", justify="right", bg="#ffd1dc", fg="#333", bd=0)
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button layout with minimalist design
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create buttons with minimalist design
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), fg="#fff", 
                       bg="#ff66b2", relief="flat", activebackground="#ff3385", bd=0,
                       command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5)

# Run the main loop
root.mainloop()