from tkinter import *
from tkinter import ttk, messagebox

def calculate_simple_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        if principal < 0 or rate < 0 or time < 0:
            messagebox.showerror("Error", "Please enter non-negative values for principal, rate, and time.")
        else:
            # Calculate simple interest
            simple_interest = (principal * rate * time) / 100

            # Calculate amount
            amount = principal + simple_interest

            # Display the results with colored text in a dialog box
            result_text = "Simple Interest: {:.2f}\nAmount: {:.2f}".format(simple_interest, amount)
            messagebox.showinfo("Calculation Result", result_text, icon="info")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for principal, rate, and time.")

# Create the main window
root = Tk()
root.title("Simple Interest Calculator")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widgets with placeholder text
principal_entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
principal_entry.insert(0, "Enter Principal")
principal_entry.bind("<FocusIn>", lambda event: principal_entry.delete(0, END))
principal_entry.grid(row=0, column=0, padx=10, pady=10)

rate_entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
rate_entry.insert(0, "Enter Rate")
rate_entry.bind("<FocusIn>", lambda event: rate_entry.delete(0, END))
rate_entry.grid(row=0, column=1, padx=10, pady=10)

time_entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
time_entry.insert(0, "Enter Time")
time_entry.bind("<FocusIn>", lambda event: time_entry.delete(0, END))
time_entry.grid(row=0, column=2, padx=10, pady=10)

# Create and place the calculate button with larger size
calculate_button = ttk.Button(root, text="Calculate", command=calculate_simple_interest, style="TButton")
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the calculate_simple_interest function
root.bind("<Return>", lambda event: calculate_simple_interest())

# Run the Tkinter event loop
root.mainloop()
