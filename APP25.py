from tkinter import *
from tkinter import ttk

def find_numbers():
    result_numbers = []

    for num in range(1500, 2701):
        if num % 7 == 0 and num % 5 == 0:
            result_numbers.append(num)

    # Clear existing items in the treeview
    for item in result_treeview.get_children():
        result_treeview.delete(item)

    # Insert the found numbers into the treeview
    for number in result_numbers:
        result_treeview.insert("", "end", values=(number,))

# Create the main window
root = Tk()
root.title("Numbers Finder")

# Create and place find numbers button
find_numbers_button = ttk.Button(root, text="Find Numbers \nwhich are divisible by 7 \nand multiples of 5, \nbetween 1500 and 2700 (both included) ", command=find_numbers)
find_numbers_button.grid(row=0, column=0, padx=20, pady=10)

# Create and place result treeview with heading
result_treeview = ttk.Treeview(root, columns=("Numbers",), show="headings")
result_treeview.heading("Numbers", text="Numbers")
result_treeview.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

# Create and place vertical scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=result_treeview.yview)
scrollbar.grid(row=1, column=1, sticky="ns", pady=10)

# Configure treeview to use the scrollbar
result_treeview.configure(yscrollcommand=scrollbar.set)

# Configure row and column weights for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the Tkinter event loop
root.mainloop()
