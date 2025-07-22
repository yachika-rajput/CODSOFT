import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create main app window
app = ctk.CTk()
app.geometry("300x400")
app.title("Simple Calculator")

# Entry field to show input/output
entry = ctk.CTkEntry(app, width=250, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Function to update entry when buttons are pressed
def button_click(value):
    entry.insert("end", value)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert("end", str(result))
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Error")

# Function to clear entry field
def clear():
    entry.delete(0, "end")

# Create calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

# Add buttons to the app
for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    elif text == 'C':
        action = clear
    else:
        action = lambda x=text: button_click(x)

    ctk.CTkButton(app, text=text, command=action, width=50).grid(row=row, column=col, padx=5, pady=5)

# Run the app
app.mainloop()
