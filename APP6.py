from tkinter import *
from tkinter import ttk

def calculate_factorial():
    try:
        num = int(entry.get())

        if num < 0:
            result_label.config(text="Error: Please enter a non-negative integer.", foreground="red")
            return

        factorial_result = 1
        steps_data = []

        for i in range(1, num + 1):
            factorial_result *= i
            steps_data.append((i, factorial_result))

        result_label.config(text="Factorial of {} is: {}".format(num, factorial_result), foreground="green")

        # Clear previous entries in the table
        for item in table.get_children():
            table.delete(item)

        # Add the calculation steps to the table
        for step in steps_data:
            table.insert("", "end", values=step)
    except ValueError:
        result_label.config(text="Error: Please enter a valid integer.", foreground="red")

# Create the main window
root = Tk()
root.title("Factorial Calculator with Table")

# Set the height of the table
table_height = 10

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widget with placeholder text
entry = ttk.Entry(root, width=10, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter a number")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the calculate factorial button with larger size
calculate_button = ttk.Button(root, text="Calculate Factorial", command=calculate_factorial, style="TButton")
calculate_button.grid(row=0, column=1, padx=10, pady=10)

# Create and place the result label
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and place the table with a vertical scroll bar
columns = ("Step", "Factorial")
table = ttk.Treeview(root, columns=columns, show="headings", height=table_height)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100, anchor=CENTER)

table.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Add a vertical scroll bar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
scrollbar.grid(row=2, column=2, sticky="ns")
table.configure(yscrollcommand=scrollbar.set)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the calculate factorial function
root.bind("<Return>", lambda event: calculate_factorial())

# Run the Tkinter event loop
root.mainloop()

