from tkinter import *
from tkinter import ttk, messagebox

def is_perfect_number(number):
    divisors_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    return divisors_sum == number

def check_perfect_number():
    try:
        input_number = int(entry.get())

        if input_number <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
        else:
            if is_perfect_number(input_number):
                messagebox.showinfo("Perfect Number Check", "{} is a perfect number.".format(input_number))
            else:
                messagebox.showinfo("Perfect Number Check", "{} is not a perfect number.".format(input_number))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = Tk()
root.title("Perfect Number Checker")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widget with placeholder text
entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter a Number")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place check perfect number button with larger size
check_button = ttk.Button(root, text="Check Perfect Number", command=check_perfect_number, style="TButton")
check_button.grid(row=1, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the check_perfect_number function
root.bind("<Return>", lambda event: check_perfect_number())

# Run the Tkinter event loop
root.mainloop()
