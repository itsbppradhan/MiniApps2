from tkinter import *
from tkinter import ttk, simpledialog, messagebox


def count_numbers():
    even_count = 0
    odd_count = 0
    negative_count = 0
    positive_count = 0
    zero_count = 0

    for entry_var in entry_vars:
        try:
            num = float(entry_var.get())
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

            if num < 0:
                negative_count += 1
            elif num > 0:
                positive_count += 1
            else:
                zero_count += 1

        except ValueError:
            continue

    result_text = "Even: {}\nOdd: {}\nNegative: {}\nPositive: {}\nZero: {}".format(
        even_count, odd_count, negative_count, positive_count, zero_count
    )

    messagebox.showinfo("Number Analysis Result", result_text)
    clear_entries()


def create_entry_bars(num_entries):
    global entry_vars

    # Clear existing widgets
    for entry in entry_vars:
        entry.destroy()

    entry_vars = []

    # Create new entry bars
    for i in range(num_entries):
        entry_var = StringVar()
        entry_vars.append(entry_var)

        entry = ttk.Entry(root, textvariable=entry_var, font=("Helvetica", 12), justify="center")
        entry.grid(row=i % 12, column=i // 12, padx=5, pady=5)

        entry.insert(0, "Enter Number")
        entry.bind("<FocusIn>", lambda event, i=i: clear_hint_text(i))
        entry.bind("<FocusOut>", lambda event, i=i: restore_hint_text(i))
        entry.bind("<Return>", lambda event, i=i: process_entry(i))


def clear_hint_text(index):
    entry_var = entry_vars[index]
    if entry_var.get() == "Enter Number":
        entry_var.set("")


def restore_hint_text(index):
    entry_var = entry_vars[index]
    if not entry_var.get():
        entry_var.set("Enter Number")


def process_entry(index):
    try:
        num = float(entry_vars[index].get())
        result_label.config(text="Entered number: {}".format(num), foreground="blue")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value.")


def clear_entries():
    for entry_var in entry_vars:
        entry_var.set("Enter Number")


def restart_program():
    root.destroy()
    python = sys.executable
    os.execl(python, python, *sys.argv)


# Create the main window
root = Tk()
root.title("Number Analysis")

# Style for larger buttons and colored text
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Ask for the number of entries using a dialog box
num_entries = simpledialog.askinteger("Number of Entries", "Enter the number of entries:")
if num_entries is None or num_entries <= 0:
    messagebox.showerror("Error", "Please enter a valid positive number of entries.")
    root.destroy()
else:
    entry_vars = []

    # Create entry bars based on the number of entries
    create_entry_bars(num_entries)

    # Create and place analyze button with larger size
    analyze_button = ttk.Button(root, text="Analyze Numbers", command=count_numbers, style="TButton")
    analyze_button.grid(row=num_entries % 12, column=(num_entries - 1) // 12 + 1, padx=5, pady=5)

    # Create and place restart button with larger size
    restart_button = ttk.Button(root, text="Restart", command=restart_program, style="TButton")
    restart_button.grid(row=(num_entries % 12) + 1, column=(num_entries - 1) // 12 + 1, padx=5, pady=5)

    # Set padding for all widgets in the window
    for child in root.winfo_children():
        child.grid_configure(padx=5, pady=5)

    # Run the Tkinter event loop
    root.mainloop()
