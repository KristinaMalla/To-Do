import tkinter as tk
from tkinter import messagebox


def create_window():
    window = tk.Tk()
    window.title("To-Do List Manager")
    window.geometry("400x300")
    return window

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def create_gui(window):
    # Task Entry
    global task_entry
    task_entry = tk.Entry(window, width=50)
    task_entry.pack(pady=20)

    # Add Button
    add_btn = tk.Button(window, text="Add Task", width=10, command=add_task)
    add_btn.pack()

    # Task Listbox
    global task_listbox
    task_listbox = tk.Listbox(window, width=50)
    task_listbox.pack(pady=10)

    # Remove Button
    remove_btn = tk.Button(window, text="Remove Task", width=10, command=remove_task)
    remove_btn.pack()

    return window

if __name__ == "__main__":
    window = create_window()
    create_gui(window)
    window.mainloop()
