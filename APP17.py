from tkinter import *
from tkinter import ttk, messagebox

def calculate_discount():
    try:
        cost = float(entry_cost.get())

        if cost >= 5000:
            discount_percentage = 10
            discount = cost * 0.1
        elif 2000 <= cost <= 4999:
            discount_percentage = 5
            discount = cost * 0.05
        else:
            discount_percentage = 0
            discount = 0

        discounted_price = cost - discount

        result_label.config(
            text="Discount: ₹{:.2f} ({:.0f}%)\nDiscounted Price: ₹{:.2f}".format(discount, discount_percentage, discounted_price),
            foreground="blue"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric cost.")

# Create the main window
root = Tk()
root.title("Product Discount Calculator")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widget with placeholder text
entry_cost = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
entry_cost.insert(0, "Enter Cost")
entry_cost.bind("<FocusIn>", lambda event: entry_cost.delete(0, END))
entry_cost.grid(row=0, column=0, padx=10, pady=10)

# Create and place calculate discount button with larger size
calculate_button = ttk.Button(root, text="Calculate Discount", command=calculate_discount, style="TButton")
calculate_button.grid(row=1, column=0, padx=10, pady=10)

# Create and place result label with colored text
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
