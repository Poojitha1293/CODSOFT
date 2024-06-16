import tkinter as tk
from tkinter import simpledialog,messagebox

def addTask():
    task=entry.get()
    if task!="":
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("OOPS!!!","You Should Enter a Task.")
        
def deleteTask():
    try:
        selected=listbox.curselection()
        if selected:
            messagebox.showwarning(selected,"Are You Sure You Want To Delete It!")
            listbox.delete(selected)
        else:
            messagebox.showwarning("OOPS!!!","You Should Select a Task To Delete!")
    except:
        messagebox.showwarning("OOPS!!!","Error Occured!")

def editTask():
    try:
        selected=listbox.curselection()
        if selected:
            task=listbox.get(selected)
            new_task=simpledialog.askstring("Edit Task","Edit Your Task : ",initialvalue=task)
            if new_task:
                listbox.delete(selected)
                listbox.insert(selected,new_task)
        else:
            messagebox.showwarning("OOPS!!!","You Should Select a Task To Edit!")
    except:
        messagebox.showwarning("OOPS!!!","Error Occured!")

system=tk.Tk()
system.title("TO-DO-LIST")
system.configure(bg='ivory')
system.geometry("600x600")

label1=tk.Label(system,text="To-Do-List",font=('Times New Roman',30,'bold'),fg='white',bg='yellow',width=90,height=2)
label1.pack()

label2=tk.Label(system,text="Enter task to perform",font=('Times New Roman',15),fg='black')
label2.place(x=10,y=130)

entry=tk.Entry(system,font=('Goudy Old Style',20),fg='black')
entry.place(x=10,y=170)

add=tk.Button(system,text="ADD",bg='blue',fg='white',font=('Arial',15),command=addTask)
add.place(x=400,y=170)

edit=tk.Button(system,text="EDIT",bg='tomato',fg='white',font=('Arial',15),command=editTask)
edit.place(x=470,y=170)

delete=tk.Button(system,text="DELETE",bg='lime green',fg='white',font=('Arial',15),command=deleteTask)
delete.place(x=550,y=170)

label3=tk.Label(system,text="Tasks To Do!!!",fg='black',font=('Times New Roman',25))
label3.place(x=10,y=240)

listbox=tk.Listbox(system,width=90,fg='white',bg='black',font=('Arial',15))
listbox.place(x=10,y=300)

system.mainloop()
