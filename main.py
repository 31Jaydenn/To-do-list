import tkinter as tk

window = tk.Tk()
window.geometry("300x300")
window.title("Da to do list")
window.configure(bg = "red")

Task_stringvar = tk.StringVar()

task_label = tk.Label(text="New Task")
task_label.place(x=40, y=190)
task_field = tk.Entry(text="", textvariable=Task_stringvar)
task_field.place(x=100, y=190)

def add_task():
  task = Task_stringvar.get()
  if task != "":
    select.insert(tk.END, task)  # Listbox
    Task_stringvar.set("")  #Empty the entry field


buttonadd = tk.Button(window, text="Add task", command=add_task)
buttonadd.place(x=10, y=10)


def delete_task():
  select.delete(tk.ANCHOR)


buttondelete = tk.Button(window, text="Delete task", command=delete_task)
buttondelete.place(x=10, y=40)


#select.itemconfig()
def task_finished():
  select.itemconfig(tk.ANCHOR, fg="green")


buttonfinished = tk.Button(window, text="Finish task", command=task_finished)
buttonfinished.place(x=10, y=70)


def clear_list():
  select.delete(0, tk.END)


buttonclear = tk.Button(window, text="Clear list", command=clear_list)
buttonclear.place(x=10, y=100)

scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)


def edit_task():
  #select a task
  #bring that task into the newtask field
  #save the new task and delete the old task

  #selected_task = select.curseselection()
  selected_task = select.get(tk.ANCHOR)
  Task_stringvar.set(selected_task)
  select.delete(tk.ANCHOR)


buttonedit = tk.Button(window, text="Edit task", command=edit_task)
buttonedit.place(x=10, y=130)

select = tk.Listbox(window, yscrollcommand=scrollbar.set)
scrollbar.config(command=select.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
select.place(x=100, y=10)
tk.mainloop()
