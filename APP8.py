from tkinter import *
from tkinter import ttk

def calculate_sum_of_digits():
    try:
        input_number = int(entry.get())
        digit_sum = sum(int(digit) for digit in str(abs(input_number)))
        result_label.config(text="Sum of digits: {}".format(digit_sum), foreground="green")
    except ValueError:
        result_label.config(text="Error: Please enter a valid integer.", foreground="red")

# Create the main window
root = Tk()
root.title("Sum of Digits Calculator")

# Style for colored text
style = ttk.Style()
style.configure("TLabel", foreground="black", font=("Helvetica", 12))

# Create and place the entry widget with placeholder text
entry = ttk.Entry(root, width=20, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter a number")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the calculate sum button with larger size
calculate_button = ttk.Button(root, text="Calculate Sum", command=calculate_sum_of_digits, style="TButton")
calculate_button.grid(row=1, column=0, padx=10, pady=10)

# Create and place the result label with colored text
result_label = Label(root, text="Sum of digits: ", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the calculate sum function
root.bind("<Return>", lambda event: calculate_sum_of_digits())

# Run the Tkinter event loop
root.mainloop()
