import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            if isinstance(result, float):
                result = round(result, 10)  # Round to handle floating-point precision issues
            expression_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            expression_var.set(expression)
    elif text == "C":
        expression = ""
        expression_var.set(expression)
    else:
        expression += text
        expression_var.set(expression)

def key_press(event):
    global expression
    key = event.char
    if key in "0123456789+-*/.":
        expression += key
        expression_var.set(expression)
    elif key == "\r":  # Enter key
        try:
            result = eval(expression)
            if isinstance(result, float):
                result = round(result, 10)  # Round to handle floating-point precision issues
            expression_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            expression_var.set(expression)
    elif key == "\x08":  # Backspace key
        expression = expression[:-1]
        expression_var.set(expression)

# Initialize main window
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("400x600")
root.configure(bg="#2c3e50")  # Set background color

# Expression variables
expression = ""
expression_var = tk.StringVar()

# Entry widget to display current expression
entry = tk.Entry(root, textvar=expression_var, font=("Arial", 24), justify='right', bd=10, relief=tk.SUNKEN, bg="#ecf0f1", fg="#2c3e50")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=20)

# Bind keyboard events
root.bind("<Key>", key_press)

# Define button layout
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Button styles
button_bg = "#34495e"
button_fg = "#ecf0f1"
button_active_bg = "#16a085"
button_active_fg = "#ffffff"

# Create buttons
for row in button_texts:
    frame = tk.Frame(root, bg="#2c3e50")
    frame.pack(expand=True, fill=tk.BOTH)
    for text in row:
        button = tk.Button(
            frame, 
            text=text, 
            font=("Arial", 20), 
            relief=tk.RAISED, 
            bd=5, 
            bg=button_bg, 
            fg=button_fg, 
            activebackground=button_active_bg, 
            activeforeground=button_active_fg
        )
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        button.bind("<Button-1>", click)

# Run the application
root.mainloop()
