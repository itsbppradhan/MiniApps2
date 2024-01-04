from tkinter import *
from tkinter import ttk

def print_even_series():
    even_series = [num for num in range(2, 51, 2)]
    display_series(even_series, "Even Numbers up to 50")

def print_odd_series():
    odd_series = []
    num = 1
    while num <= 25:
        odd_series.append(num)
        num += 2
    display_series(odd_series, "Odd Numbers up to 25")

def display_series(series, title):
    result_table.delete(*result_table.get_children())
    for index, value in enumerate(series):
        result_table.insert("", "end", values=(index + 1, value))
    result_label.config(text=title, foreground="blue")

# Create the main window
root = Tk()
root.title("Number Series Printer")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place print even series button with larger size
print_even_button = ttk.Button(root, text="Print Even Series", command=print_even_series, style="TButton")
print_even_button.grid(row=0, column=0, padx=10, pady=10)

# Create and place print odd series button with larger size
print_odd_button = ttk.Button(root, text="Print Odd Series", command=print_odd_series, style="TButton")
print_odd_button.grid(row=0, column=1, padx=10, pady=10)

# Create and place result label with colored text
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create result table with colored text and add a vertical scroll bar
columns = ("Index", "Value")
result_table = ttk.Treeview(root, columns=columns, show="headings", height=10)

for col in columns:
    result_table.heading(col, text=col)
    result_table.column(col, width=100, anchor=CENTER)

result_table.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Add a vertical scroll bar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=result_table.yview)
scrollbar.grid(row=2, column=2, sticky="ns")
result_table.configure(yscrollcommand=scrollbar.set)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Configure weights to allow table resizing
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the Tkinter event loop
root.mainloop()
