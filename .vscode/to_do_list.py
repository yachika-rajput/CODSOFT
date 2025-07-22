import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 My Daily To-Do")
        self.root.geometry("400x500")
        self.tasks = []

        self.task_var = tk.StringVar()

        # Input field and Add Task button
        tk.Entry(root, textvariable=self.task_var, width=30, font=("Arial", 12)).pack(pady=10)
        tk.Button(root, text="+ Add Task", width=20, bg="green", fg="white", command=self.add_task).pack(pady=5)

        # Task list frame
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)

        # Buttons
        tk.Button(root, text="✔ COMPLETE", bg="green", fg="white", width=20, command=self.mark_completed).pack(pady=5)
        tk.Button(root, text="🗑 DELETE", bg="red", fg="white", width=20, command=self.delete_task).pack(pady=5)

        # Status bar
        self.status_label = tk.Label(root, text="Total: 0  Completed: 0  Incomplete: 0", font=("Arial", 10))
        self.status_label.pack(pady=10)


    def add_task(self):
        task_text = self.task_var.get().strip()
        if task_text == "":
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return

        task = {"text": task_text, "var": tk.BooleanVar()}
        self.tasks.append(task)
        self.task_var.set("")
        self.refresh_tasks()
        
    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            var = task["var"]
            cb = tk.Checkbutton(self.task_frame, text=task["text"], variable=var, anchor="w", width=30)
            cb.grid(row=i, sticky="w")

        self.update_status()

    def mark_completed(self):
        self.refresh_tasks()  # No special action needed, checkbox itself stores the state

    def delete_task(self):
        self.tasks = [t for t in self.tasks if not t["var"].get()]
        self.refresh_tasks()

    def update_status(self):
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["var"].get())
        incomplete = total - completed
        self.status_label.config(text=f"Total: {total}  Completed: {completed}  Incomplete: {incomplete}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
