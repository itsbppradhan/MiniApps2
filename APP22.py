from tkinter import *
from tkinter import ttk, messagebox

def count_odd_even_digits():
    try:
        number = int(entry_number.get())
        odd_count = 0
        even_count = 0

        for digit in str(abs(number)):
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        result_label.config(text=f"Odd Digits: {odd_count}, Even Digits: {even_count}", foreground="blue")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = Tk()
root.title("Odd and Even Digit Counter")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widget for number input
entry_number = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry_number.insert(0, "Enter Number")
entry_number.bind("<FocusIn>", lambda event: entry_number.delete(0, END))
entry_number.bind("<Return>", lambda event: count_odd_even_digits())
entry_number.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Create and place count button with larger size
count_button = ttk.Button(root, text="Count Odd and Even Digits", command=count_odd_even_digits, style="TButton")
count_button.grid(row=1, column=0, padx=10, pady=10, sticky=W)

# Create and place result label with colored text
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
