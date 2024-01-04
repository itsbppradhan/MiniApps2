from tkinter import *
from tkinter import ttk, messagebox

def calculate_hcf_lcm(*args):
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())

        if num1 <= 0 or num2 <= 0:
            messagebox.showerror("Error", "Please enter positive integers.")
            return

        # Calculate HCF
        hcf_result = hcf(num1, num2)

        # Calculate LCM
        lcm_result = lcm(num1, num2)

        # Display results in a table with colored text
        result_table.delete(*result_table.get_children())
        result_table.insert("", "end", values=("HCF", hcf_result))
        result_table.insert("", "end", values=("LCM", lcm_result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")

def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // hcf(a, b)

def focus_next_entry(event, next_entry):
    event.widget.tk_focusNext().focus()
    return "break"

# Create the main window
root = Tk()
root.title("HCF and LCM Calculator")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widgets with placeholder text
entry_num1 = ttk.Entry(root, width=10, font=("Helvetica", 14), justify="center")
entry_num1.insert(0, "Enter Number 1")
entry_num1.bind("<FocusIn>", lambda event: entry_num1.delete(0, END))
entry_num1.bind("<Return>", lambda event: focus_next_entry(event, entry_num2))
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = ttk.Entry(root, width=10, font=("Helvetica", 14), justify="center")
entry_num2.insert(0, "Enter Number 2")
entry_num2.bind("<FocusIn>", lambda event: entry_num2.delete(0, END))
entry_num2.bind("<Return>", lambda event: calculate_hcf_lcm())
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Create and place calculate button with larger size
calculate_button = ttk.Button(root, text="Calculate HCF and LCM", command=calculate_hcf_lcm, style="TButton")
calculate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and place result table with colored text
columns = ("Property", "Result")
result_table = ttk.Treeview(root, columns=columns, show="headings", height=2)

for col in columns:
    result_table.heading(col, text=col)
    result_table.column(col, width=100, anchor=CENTER)

result_table.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Configure weights to allow table resizing
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the Tkinter event loop
root.mainloop()
