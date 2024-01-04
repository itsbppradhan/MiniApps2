from tkinter import *
from tkinter import ttk

def check_number():
    try:
        input_number = int(entry.get())
        result = ""

        # Check if the number is odd or even
        result += "Odd" if input_number % 2 != 0 else "Even"

        # Check if the number is positive or negative
        result += ", Positive" if input_number > 0 else ", Negative" if input_number < 0 else ""

        # Add the result to the table
        table.insert("", "end", values=(input_number, result))
        result_label.config(text="Result: {} is {}.".format(input_number, result), foreground="green")

    except ValueError:
        result_label.config(text="Error: Please enter a valid integer.", foreground="red")

# Create the main window
root = Tk()
root.title("Number Checker")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widget with placeholder text
entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter an integer")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)


# Create and place the check number button with larger size
check_button = ttk.Button(root, text="Check Number", command=check_number, style="TButton")
check_button.grid(row=1, column=0, padx=10, pady=10)

# Create and place the result label
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10)

# Create and place the table
columns = ("Number", "Result")
table = ttk.Treeview(root, columns=columns, show="headings", height=5)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100, anchor=CENTER)

table.grid(row=3, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the check function
root.bind("<Return>", lambda event: check_number())

# Run the Tkinter event loop
root.mainloop()
