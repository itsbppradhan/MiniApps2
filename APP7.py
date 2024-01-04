from tkinter import *
from tkinter import ttk, messagebox


def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)

    # Check if the string is the same when read forward and backward
    return num_str == num_str[::-1]


def check_palindrome():
    try:
        input_number = int(entry.get())

        if is_palindrome(input_number):
            messagebox.showinfo("Palindrome Check", "{} is a palindrome number.".format(input_number))
        else:
            messagebox.showinfo("Palindrome Check", "{} is not a palindrome number.".format(input_number))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")


# Create the main window
root = Tk()
root.title("Palindrome Checker")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widget with placeholder text
entry = ttk.Entry(root, width=20, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter a number")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the check palindrome button with ttk style
check_button = ttk.Button(root, text="Check Palindrome", command=check_palindrome, style="TButton")
check_button.grid(row=1, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the check_palindrome function
root.bind("<Return>", lambda event: check_palindrome())

# Run the Tkinter event loop
root.mainloop()
