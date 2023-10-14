import tkinter as tk

# Function to update the display with button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to perform calculations
def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry field for displaying input and results
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button_text in button_texts:
    tk.Button(root, text=button_text, padx=20, pady=20, command=lambda button_text=button_text: button_click(button_text) if button_text != "=" else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button
clear_button = tk.Button(root, text="C", padx=20, pady=20, command=clear)
clear_button.grid(row=row_val, column=col_val)

root.mainloop()
