from tkinter import *
from tkinter import ttk

def sum_of_square_of_odd_digits(number):
    sum_of_odd_digits = 0

    while number > 0:
        digit = number % 10

        if digit % 2 != 0:
            sum_of_odd_digits += digit

        number = number // 10

    sum_squared = sum_of_odd_digits ** 2

    return sum_squared

def calculate_result(*args):
    try:
        input_number = int(entry.get())

        if 10000 <= input_number <= 99999:
            result = sum_of_square_of_odd_digits(input_number)
            result_label.config(text="Sum of the square of odd digits: {}".format(result), foreground="green")
        else:
            result_label.config(text="Please enter a 5-digit integer.", foreground="red")
    except ValueError:
        result_label.config(text="Please enter a valid integer.", foreground="red")

# Create the main window
root = Tk()
root.title("Sum of Squares of Odd Digits")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widget with placeholder text
entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter a number")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the calculate button with larger size
calculate_button = ttk.Button(root, text="Calculate", command=calculate_result, style="TButton")
calculate_button.grid(row=0, column=1, padx=10, pady=10)

# Create and place the result label
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the calculate function
root.bind("<Return>", calculate_result)

# Run the Tkinter event loop
root.mainloop()
