import tkinter as tk
from tkinter import messagebox,simpledialog

class TodoListApp:
    def __init__(self,root):
        self.root= root
        self.root.title("To-do List Application")


        self.tasks= []
        self.load_tasks()

        self.task_listbox =tk.Listbox(root,width= 60,height=15,selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        add_task_button =tk.Button(root,text="Add Task", command=self.add_task)
        add_task_button.pack(pady=5)

        remove_task_button =tk.Button(root,text="Remove Task", command=self.remove_task)
        remove_task_button.pack(pady=5)

        update_task_button= tk.Button(root,text="Update Task",command=self.update_task)
        update_task_button.pack(pady=5)

        complete_task_button= tk.Button(root,text="Complete Task",command=self.complete_task)
        complete_task_button.pack(pady=5)

        self.update_task_listbox()


    def add_task(self):
        task= simpledialog.askstring("Add Task", "Enter task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.save_tasks()


    def remove_task(self):
        selected_index =self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.update_task_listbox()
            self.save_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index =selected_index[0]
            new_task =simpledialog.askstring("Update Task", "Enter new task:", initialvalue= self.tasks[task_index]["task"])
            if new_task:
                self.tasks[task_index]["task"] =new_task
                self.update_task_listbox()
                self.save_tasks()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index]["completed"] =True
            self.update_task_listbox()
            self.save_tasks()

    def update_task_listbox(self):
        self.task_listbox.delete(0,tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.task_listbox.insert(tk.END, "[X] " + task["task"])
            else:
                self.task_listbox.insert(tk.END, "[ ] " + task["task"])

    def save_tasks(self):
        with open("task.txt", "w") as f:
            for task in self.tasks:
                f.write(task["task"] + "," + str(task["completed"]) + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task_info = line.strip().split(",")
                    task = {"task": task_info[0], "completed": bool(task_info[1])}
                    self.tasks.append(task)

            self.update_task_listbox()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root= tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
            
            
