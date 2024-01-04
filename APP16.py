from tkinter import *
from tkinter import ttk, messagebox

def is_armstrong_number(number):
    num_digits = len(str(number))
    temp_number = number
    sum_of_digits = 0

    while temp_number > 0:
        digit = temp_number % 10
        sum_of_digits += digit ** num_digits
        temp_number //= 10

    return sum_of_digits == number

def check_armstrong_number():
    try:
        input_number = int(entry.get())

        if input_number < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer.")
        else:
            if is_armstrong_number(input_number):
                messagebox.showinfo("Armstrong Number Check", "{} is an Armstrong number.".format(input_number))
            else:
                messagebox.showinfo("Armstrong Number Check", "{} is not an Armstrong number.".format(input_number))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = Tk()
root.title("Armstrong Number Checker")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widget with placeholder text
entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter a Number")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place check Armstrong number button with larger size
check_button = ttk.Button(root, text="Check Armstrong Number", command=check_armstrong_number, style="TButton")
check_button.grid(row=1, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the check_armstrong_number function
root.bind("<Return>", lambda event: check_armstrong_number())

# Run the Tkinter event loop
root.mainloop()
