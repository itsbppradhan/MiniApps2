from tkinter import *
from tkinter import ttk, messagebox


def is_spy_number(number):
    digit_list = [int(digit) for digit in str(abs(number))]
    digit_sum = sum(digit_list)
    digit_product = 1 if not digit_list else 1
    for digit in digit_list:
        digit_product *= digit
    return digit_sum == digit_product


def check_spy_number():
    try:
        input_number = int(entry.get())

        if is_spy_number(input_number):
            messagebox.showinfo("Spy Number Check", "{} is a Spy number.".format(input_number))
        else:
            messagebox.showinfo("Spy Number Check", "{} is not a Spy number.".format(input_number))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")


# Create the main window
root = Tk()
root.title("Spy Number Checker")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widget with placeholder text
entry = ttk.Entry(root, width=20, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter a number")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the check spy number button with ttk style
check_button = ttk.Button(root, text="Check Spy Number", command=check_spy_number, style="TButton")
check_button.grid(row=1, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the check_spy_number function
root.bind("<Return>", lambda event: check_spy_number())

# Run the Tkinter event loop
root.mainloop()
