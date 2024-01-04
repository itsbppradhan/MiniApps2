from tkinter import *
from tkinter import ttk

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif 80 <= marks <= 89:
        return "B"
    elif 70 <= marks <= 79:
        return "C"
    elif 60 <= marks <= 69:
        return "D"
    else:
        return "E"

def calculate_grade(*args):
    try:
        marks = int(entry.get())

        if 0 <= marks <= 100:
            grade = get_grade(marks)
            result_label.config(text="Grade: {}".format(grade), foreground="green")
        else:
            result_label.config(text="Please enter a valid mark between 0 and 100.", foreground="red")
    except ValueError:
        result_label.config(text="Please enter a valid integer.", foreground="red")

# Create the main window
root = Tk()
root.title("Grade Calculator")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widget with placeholder text
entry = ttk.Entry(root, width=15, font=("Helvetica", 14), justify="center")
entry.insert(0, "Enter marks")
entry.bind("<FocusIn>", lambda event: entry.delete(0, END))
entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the calculate button with larger size
calculate_button = ttk.Button(root, text="Calculate Grade", command=calculate_grade, style="TButton")
calculate_button.grid(row=0, column=1, padx=10, pady=10)

# Create and place the result label
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Bind the Enter key to the calculate function
root.bind("<Return>", calculate_grade)

# Run the Tkinter event loop
root.mainloop()
