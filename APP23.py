from tkinter import *
from tkinter import ttk, messagebox

def find_largest_digit():
    try:
        number = int(entry_number.get())

        largest_digit = max(map(int, str(abs(number))))

        result_label.config(text=f"Largest Digit: {largest_digit}", foreground="blue")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = Tk()
root.title("Largest Digit Finder")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widget for number input
entry_number = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry_number.insert(0, "Enter Number")
entry_number.bind("<FocusIn>", lambda event: entry_number.delete(0, END))
entry_number.bind("<Return>", lambda event: find_largest_digit())
entry_number.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Create and place find button with larger size
find_button = ttk.Button(root, text="Find Largest Digit", command=find_largest_digit, style="TButton")
find_button.grid(row=1, column=0, padx=10, pady=10, sticky=W)

# Create and place result label with colored text
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
