from tkinter import *
from tkinter import ttk, messagebox

def check_character(event=None):
    character = entry_character.get()

    if character.isdigit():
        result_label.config(text=f"The entered character '{character}' is a digit.", foreground="blue")
    elif character.lower() in "aeiou":
        result_label.config(text=f"The entered character '{character}' is a vowel.", foreground="green")
    else:
        result_label.config(text=f"The entered character '{character}' is neither a vowel nor a digit.", foreground="red")

# Create the main window
root = Tk()
root.title("Character Checker")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Create and place entry widget for character input
entry_character = ttk.Entry(root, font=("Helvetica", 14), justify="center")
entry_character.insert(0, "Enter Character")
entry_character.bind("<FocusIn>", lambda event: entry_character.delete(0, END))
entry_character.bind("<Return>", check_character)  # Map Enter key to the check_character function
entry_character.grid(row=0, column=0, padx=10, pady=10)

# Create and place check button with larger size
check_button = ttk.Button(root, text="Check Character", command=check_character, style="TButton")
check_button.grid(row=1, column=0, padx=10, pady=10)

# Create and place result label with colored text
result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, padx=10, pady=10)

# Set padding for all widgets in the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
