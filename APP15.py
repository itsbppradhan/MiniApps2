from tkinter import *
from tkinter import ttk

def calculate_series():
    series_sum = 0
    current_term = 1

    for _ in range(6):  # Loop for 6 terms (1+11+111+1111+11111+111111)
        series_sum += current_term
        current_term = current_term * 10 + 1

    result_label.config(text="Sum of the series: {}".format(series_sum), foreground="blue")

# Create the main window
root = Tk()
root.title("Series Calculator")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place title label
title_label = Label(root, text="Calculate Series", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create and place calculate series button with larger size
calculate_button = ttk.Button(root, text="Calculate Series 1+11+...+111111", command=calculate_series, style="TButton")
calculate_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

# Create and place result label with colored text
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Configure weights to allow title label resizing
root.grid_rowconfigure(0, weight=1)

# Run the Tkinter event loop
root.mainloop()
