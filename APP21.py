from tkinter import *
from tkinter import ttk, messagebox

def calculate_ticket_price():
    try:
        age = int(entry_age.get())

        if age < 5 or age > 60:
            ticket_price = 0
        elif 5 <= age <= 15:
            ticket_price = 100
        else:
            ticket_price = 200

        result_label.config(text=f"Ticket Price: {ticket_price} Rs", foreground="blue")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age.")

# Create the main window
root = Tk()
root.title("Movie Ticket Price Calculator")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widget for age input
entry_age = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry_age.insert(0, "Enter Age")
entry_age.bind("<FocusIn>", lambda event: entry_age.delete(0, END))
entry_age.bind("<Return>", lambda event: calculate_ticket_price())
entry_age.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Create and place calculate button with larger size
calculate_button = ttk.Button(root, text="Calculate Ticket Price", command=calculate_ticket_price, style="TButton")
calculate_button.grid(row=1, column=0, padx=10, pady=10, sticky=W)

# Create and place result label with colored text
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
