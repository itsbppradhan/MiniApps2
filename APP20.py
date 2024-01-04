from tkinter import *
from tkinter import ttk, messagebox

def generate_fibonacci():
    try:
        n = int(entry_n.get())
        if n <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return

        a, b = 0, 1
        fib_series = [1]  # Starting with 1 as the first number in the series

        for _ in range(1, n):
            a, b = b, a + b
            fib_series.append(b)

        update_table(fib_series)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

def update_table(fib_series):
    # Clear existing items in the table
    for item in table.get_children():
        table.delete(item)

    # Insert new items in the table
    for i, value in enumerate(fib_series):
        table.insert("", "end", values=(value,))


# Create the main window
root = Tk()
root.title("Fibonacci Series")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widget for n terms input
entry_n = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry_n.insert(0, "Enter req. nos.")
entry_n.bind("<FocusIn>", lambda event: entry_n.delete(0, END))
entry_n.bind("<Return>", lambda event: generate_fibonacci())
entry_n.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Create and place generate button with larger size
generate_button = ttk.Button(root, text="Generate Fibonacci", command=generate_fibonacci, style="TButton")
generate_button.grid(row=0, column=1, padx=10, pady=10, sticky=W)

# Create and place table with a scroll bar
table_frame = Frame(root)
table_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tree_columns = ("Fibonacci Series",)
table = ttk.Treeview(table_frame, columns=tree_columns, show="headings")

table.heading("Fibonacci Series", text="Fibonacci Series")
table.column("Fibonacci Series", width=200)

table_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscroll=table_scroll.set)

table.grid(row=0, column=0, padx=5, pady=5)
table_scroll.grid(row=0, column=1, sticky="ns")

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
