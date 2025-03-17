import tkinter as tk

def check_even_odd():
    try:
        num = int(entry.get())
        if num % 2 == 0:
            result_label.config(text=f"{num} is an even number.")
        else:
            result_label.config(text=f"{num} is an odd number.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def on_enter(event):
    event.widget.config(bg='lightblue')

def on_leave(event):
    event.widget.config(bg='SystemButtonFace')

root = tk.Tk()
root.title("Even and Odd Checker")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

welcome_label = tk.Label(frame, text="Welcome to Even and Odd", font=("Helvetica", 16))
welcome_label.pack(pady=5)

entry_label = tk.Label(frame, text="Enter a number:")
entry_label.pack(pady=5)

entry = tk.Entry(frame)
entry.pack(pady=5)

check_button = tk.Button(frame, text="Check", command=check_even_odd)
check_button.pack(pady=5)

result_label = tk.Label(frame, text="", font=("Helvetica", 14))
result_label.pack(pady=5)

# Adding hover effects
check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)

root.mainloop()