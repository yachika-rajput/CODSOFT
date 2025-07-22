import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
label_length = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
label_length.pack(pady=10)

entry_length = tk.Entry(root, font=("Arial", 12), justify="center")
entry_length.pack()

btn_generate = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="green", fg="white")
btn_generate.pack(pady=10)

entry_password = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
entry_password.pack(pady=10)

# Run the app
root.mainloop()