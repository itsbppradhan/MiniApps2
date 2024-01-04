from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_leap_year():
    try:
        input_year = int(entry.get())
        result = is_leap_year(input_year)

        if result:
            messagebox.showinfo("Leap Year Check", "{} is a leap year.".format(input_year))
        else:
            messagebox.showinfo("Leap Year Check", "{} is not a leap year.".format(input_year))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year.")

# Create the main window
root = Tk()
root.title("Leap Year Checker")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widget with placeholder text
entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter year")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the check leap year button with larger size
check_button = ttk.Button(root, text="Check Leap Year", command=check_leap_year, style="TButton")
check_button.grid(row=1, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the check function
root.bind("<Return>", lambda event: check_leap_year())

# Run the Tkinter event loop
root.mainloop()
