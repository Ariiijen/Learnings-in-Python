import tkinter as tk
from tkinter import messagebox

def place_order():
    menu = menu_var.get()
    choice = choice_var.get()
    
    snacks = {1: ('Cheesy Burger Meal', 50), 2: ('Crunchy Chicken Sandwich', 60), 3: ('Jolly Hotdog Meal', 40)}
    meals = {1: ('Burger Steak', 80), 2: ('Chickenjoy Rice Meal', 100), 3: ('Cornedbeef Breakfast Meal', 70)}
    
    if menu == 'Snacks':
        order = snacks.get(choice, None)
    elif menu == 'Meals':
        order = meals.get(choice, None)
    else:
        messagebox.showerror("Error", "Invalid menu choice. Please select Snacks or Meals.")
        return
    
    if order:
        messagebox.showinfo("Order Confirmed", f"Your order is {order[0]} that costs Php {order[1]:.2f}.\nThank you for ordering! Have a great day! ^^")
    else:
        messagebox.showerror("Error", "Invalid choice. Please select a valid option.")

# Create main window
root = tk.Tk()
root.title("Food Ordering System")
root.geometry("400x300")

tk.Label(root, text="Menu:", font=("Arial", 12, "bold")).pack()
tk.Label(root, text="====== Snacks ======", font=("Arial", 10, "bold")).pack()
tk.Label(root, text="1. Cheesy Burger Meal | Php 50.00").pack()
tk.Label(root, text="2. Crunchy Chicken Sandwich | Php 60.00").pack()
tk.Label(root, text="3. Jolly Hotdog Meal | Php 40.00").pack()

tk.Label(root, text="====== Meals ======", font=("Arial", 10, "bold")).pack()
tk.Label(root, text="1. Burger Steak | Php 80.00").pack()
tk.Label(root, text="2. Chickenjoy Rice Meal | Php 100.00").pack()
tk.Label(root, text="3. Cornedbeef Breakfast Meal | Php 70.00").pack()

# Menu selection dropdown
menu_var = tk.StringVar()
menu_var.set("Snacks")
tk.Label(root, text="Select Menu:").pack()
tk.OptionMenu(root, menu_var, "Snacks", "Meals").pack()

# Choice selection entry
choice_var = tk.IntVar()
tk.Label(root, text="Enter choice (1-3):").pack()
tk.Entry(root, textvariable=choice_var).pack()

# Order button
tk.Button(root, text="Place Order", command=place_order).pack()

root.mainloop()
