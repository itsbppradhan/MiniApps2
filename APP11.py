from tkinter import *
from tkinter import ttk

def calculate_sum():
    # Calculate the sum of the first 200 even natural numbers
    even_sum = sum(range(2, 401, 2))

    # Display the result
    result_label.config(text="Sum of the first 200 even natural numbers: {}".format(even_sum), foreground="green")

# Create the main window
root = Tk()
root.title("Sum of First 200 Even Natural Numbers")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the calculate button with larger size
calculate_button = ttk.Button(root, text="Calculate Sum of first 200 even natural numbers", command=calculate_sum, style="TButton")
calculate_button.grid(row=0, column=0, padx=10, pady=10)

# Create and place the result label
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
