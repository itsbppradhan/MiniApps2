from tkinter import *
from tkinter import ttk

def focus_next_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"

def find_maximum():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())

        maximum = max(num1, num2, num3)

        result_label.config(text="Maximum of {}, {}, and {} is: {}".format(num1, num2, num3, maximum), foreground="green")

        # Add the result to the table
        table.insert("", "end", values=(num1, num2, num3, maximum))
    except ValueError:
        result_label.config(text="Error: Please enter valid integers for all three numbers.", foreground="red")

# Create the main window
root = Tk()
root.title("Maximum Finder with Table")

# Style for larger buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place the entry widgets with placeholder text
entry1 = ttk.Entry(root, width=10, font=("Helvetica", 14), justify="center")
entry1.insert(0, "Enter num1")
entry1.bind("<FocusIn>", lambda event: entry1.delete(0, END))
entry1.grid(row=0, column=0, padx=10, pady=10)
entry1.bind("<Return>", focus_next_entry)

entry2 = ttk.Entry(root, width=10, font=("Helvetica", 14), justify="center")
entry2.insert(0, "Enter num2")
entry2.bind("<FocusIn>", lambda event: entry2.delete(0, END))
entry2.grid(row=0, column=1, padx=10, pady=10)
entry2.bind("<Return>", focus_next_entry)

entry3 = ttk.Entry(root, width=10, font=("Helvetica", 14), justify="center")
entry3.insert(0, "Enter num3")
entry3.bind("<FocusIn>", lambda event: entry3.delete(0, END))
entry3.grid(row=0, column=2, padx=10, pady=10)
entry3.bind("<Return>", lambda event: find_maximum())

# Create and place the find maximum button with larger size
find_button = ttk.Button(root, text="Find Maximum", command=find_maximum, style="TButton")
find_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Create and place the result label
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Create and place the table with a vertical scroll bar
columns = ("Num1", "Num2", "Num3", "Maximum")
table = ttk.Treeview(root, columns=columns, show="headings", height=5)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=80, anchor=CENTER)

table.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Add a vertical scroll bar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
scrollbar.grid(row=3, column=3, sticky="ns")
table.configure(yscrollcommand=scrollbar.set)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
