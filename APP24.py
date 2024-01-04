from tkinter import *
from tkinter import ttk, messagebox
import cmath

def move_to_next_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"

def solve_quadratic_equation(event=None):
    try:
        # Get coefficients from user input
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Calculate the discriminant
        discriminant = b**2 - 4*a*c

        # Determine the nature of roots
        if discriminant >= 0:
            nature = "Real Roots"
        else:
            nature = "Imaginary Roots"

        # Calculate roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

        # Display the roots and nature
        result_label.config(text=f"Root 1: {root1}\nRoot 2: {root2}\nNature: {nature}", foreground="blue")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical coefficients.")

# Create the main window
root = Tk()
root.title("Quadratic Equation Solver")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widgets for coefficients input in a traditional format
entry_a = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry_a.insert(0, "Enter coefficient of x²")
entry_a.bind("<FocusIn>", lambda event: entry_a.delete(0, END))
entry_a.bind("<Return>", move_to_next_entry)
entry_a.grid(row=0, column=0, padx=10, pady=10)

label_x_squared = Label(root, text=" x² + ", font=("Helvetica", 14))
label_x_squared.grid(row=0, column=1, padx=5, pady=10)

entry_b = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry_b.insert(0, "Enter coefficient of x")
entry_b.bind("<FocusIn>", lambda event: entry_b.delete(0, END))
entry_b.bind("<Return>", move_to_next_entry)
entry_b.grid(row=0, column=2, padx=10, pady=10)

label_x = Label(root, text=" x + ", font=("Helvetica", 14))
label_x.grid(row=0, column=3, padx=5, pady=10)

entry_c = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry_c.insert(0, "Enter constant term")
entry_c.bind("<FocusIn>", lambda event: entry_c.delete(0, END))
entry_c.bind("<Return>", solve_quadratic_equation)
entry_c.grid(row=0, column=4, padx=10, pady=10)

# Create and place find roots button with larger size
find_roots_button = ttk.Button(root, text="Find Roots", command=solve_quadratic_equation, style="TButton")
find_roots_button.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Create and place result label with colored text
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
