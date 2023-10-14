import tkinter as tk
from tkinter import simpledialog

task_number = 1  # Initialize the task number

def add_task():
    global task_number
    task = simpledialog.askstring("Add Task", "Enter a task:")
    if task:
        task_with_number = f"{task_number}. {task}"
        listbox.insert(tk.END, task_with_number)
        task_number += 1

def remove_task():
    selected_task = listbox.get(tk.ACTIVE)
    if selected_task:
        listbox.delete(tk.ACTIVE)

def toggle_done():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task = listbox.get(selected_task_index[0])
        if "✓" not in selected_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, f"✓ {selected_task}")
        else:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, selected_task[2:])

root = tk.Tk()
root.title("To-Do List")

# Increase the window size
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, selectbackground="yellow")
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
done_button = tk.Button(root, text="Mark as Done", command=toggle_done)

add_button.pack(pady=10)
remove_button.pack()
done_button.pack()

root.mainloop()
