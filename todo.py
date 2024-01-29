import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.configure(bg="#f0f0f0")

        self.todo_list = []

        self.task_label = tk.Label(root, text="Task:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 12))
        self.task_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.task_entry = tk.Entry(root, width=50, bg="white", fg="#333333", font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=1, padx=10, pady=5)

        self.priority_label = tk.Label(root, text="Priority:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 12))
        self.priority_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.priority_var = tk.StringVar(root)
        self.priority_var.set("Low")
        self.priority_menu = tk.OptionMenu(root, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.config(bg="white", fg="#333333", font=("Helvetica", 12))
        self.priority_menu.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4caf50", fg="white", font=("Helvetica", 12))
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        self.task_display = tk.Listbox(root, height=10, width=50, bg="white", fg="#333333", font=("Helvetica", 12))
        self.task_display.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.remove_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete, bg="#2196f3", fg="white", font=("Helvetica", 12))
        self.complete_button.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        self.todo_list.append((task, priority))
        self.update_task_display()
        messagebox.showinfo("Task Added", "Task added successfully!")
        self.task_entry.delete(0, tk.END)

    def update_task_display(self):
        self.todo_list.sort(key=lambda task: ("High", "Medium", "Low").index(task[1]))
        self.task_display.delete(0, tk.END)
        for task, priority in self.todo_list:
            self.task_display.insert(tk.END, f"{task} - Priority: {priority}")

    def mark_complete(self):
        selected_index = self.task_display.curselection()
        if selected_index:
            task_index = selected_index[0]
            task, priority = self.todo_list[task_index]
            updated_task = f"{task} - Priority: {priority} (Completed)"
            self.todo_list[task_index] = (updated_task, priority)
            self.update_task_display()
            messagebox.showinfo("Task Completed", "Task marked as completed!")
        else:
            messagebox.showerror("Error", "Please select a task to mark as completed.")

    def remove_task(self):
        selected_index = self.task_display.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.todo_list[task_index]
            self.update_task_display()
            messagebox.showinfo("Task Removed", "Task removed successfully!")
        else:
            messagebox.showerror("Error", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


'''
Older Code without colors

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")

        self.todo_list = []

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.grid(row=0, column=0, padx=10, pady=5)

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=1, padx=10, pady=5)

        self.priority_label = tk.Label(root, text="Priority:")
        self.priority_label.grid(row=1, column=0, padx=10, pady=5)

        self.priority_var = tk.StringVar(root)
        self.priority_var.set("Low")
        self.priority_menu = tk.OptionMenu(root, self.priority_var, "Low", "Medium", "High")
        self.priority_menu.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.task_display = tk.Listbox(root, height=10, width=50)
        self.task_display.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=4, column=0, padx=10, pady=5)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.grid(row=4, column=1, padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        self.todo_list.append((task, priority))
        self.update_task_display()
        messagebox.showinfo("Task Added", "Task added successfully!")
        self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_index = self.task_display.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.todo_list[task_index]
            self.update_task_display()
            messagebox.showinfo("Task Removed", "Task removed successfully!")
        else:
            messagebox.showerror("Error", "Please select a task to remove.")

    def mark_complete(self):
        selected_index = self.task_display.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.todo_list[task_index]
            self.update_task_display()
            messagebox.showinfo("Task Completed", "Task marked as completed!")
        else:
            messagebox.showerror("Error", "Please select a task to mark as completed.")

    def update_task_display(self):
        self.task_display.delete(0, tk.END)
        for task, priority in self.todo_list:
            self.task_display.insert(tk.END, f"{task} - Priority: {priority}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
'''

