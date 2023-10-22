import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog  # Added for editing tasks

# Create the main application window
app = tk.Tk()
app.title("To-Do List App")

# Initialize a list to store tasks
tasks = []

# Function to add a new task
def add_task():
    task_text = task_entry.get()
    if task_text:
        tasks.append({"text": task_text, "complete": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        del tasks[selected_task_index[0]]
        update_task_list()

# Function to edit a selected task
def edit_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        current_text = tasks[selected_task_index[0]]["text"]
        new_task_text = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=current_text)
        if new_task_text is not None:
            tasks[selected_task_index[0]]["text"] = new_task_text
            update_task_list()

# Function to mark a task as complete or incomplete
def toggle_complete():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["complete"] = not tasks[selected_task_index[0]]["complete"]
        update_task_list()

# Function to update the task listbox
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_status = "[X] " if task["complete"] else "[ ] "
        task_listbox.insert(tk.END, task_status + task["text"])

# Entry widget for entering tasks
task_entry = tk.Entry(app)
task_entry.pack(pady=10)

# Button to add tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Button to remove tasks
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack()

# Button to edit tasks
edit_button = tk.Button(app, text="Edit Task", command=edit_task)
edit_button.pack()

# Button to mark/unmark tasks as complete
complete_button = tk.Button(app, text="Mark/Unmark Complete", command=toggle_complete)
complete_button.pack()

# Listbox to display tasks
task_listbox = tk.Listbox(app)
task_listbox.pack()

# Run the application
app.mainloop()