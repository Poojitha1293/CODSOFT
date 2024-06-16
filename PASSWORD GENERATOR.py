import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

def Generate_pw():
    global password
    try:
        if entry1.get() and entry2.get():
            entry3.delete(0,END)
            length=int(entry2.get())
            l=string.ascii_letters+string.digits+string.punctuation
            password=''.join(random.choice(l) for i in range(length))
            entry3.insert(0,password)
        elif entry2.get():
            messagebox.showwarning("Warning","Please Enter User Name!!!")
        else:
            messagebox.showwarning("Warning","Please Enter length of the Password!!!")
    except ValueError:
        print("Please enter a valid integer for the password length!!!")
        
def Reset_pw():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    label5.config(text="")
    label6.config(text="")
    
    
def Accept_pw():
    global password
    if entry3.get() and entry1.get():
        s="Hi "+entry1.get()+"! your Password is : "+entry3.get()
        label5.config(text=s)
    if entry3.get()=="":
        messagebox.showwarning("Generate password!","Please Generate Password to Accept it")
    
def Copy_pw():
    if entry3.get():
        pyperclip.copy(entry3.get())
        label6.config(text="Copied Password is : "+pyperclip.paste())
    else:
        messagebox.showerror(title="Error",message="Please generate the Password to Copy!!")

system=tk.Tk()
system.title("Password Generator")
system.geometry("500x500")
system.configure(bg="light yellow")

label1=tk.Label(system,text="PASSWORD GENERATOR",font=("Goudy Old Style",30,"bold"),bg="lime green",fg="white",width=60,height=2)
label1.pack()

label2=tk.Label(system,text="Enter Username  ",font=("Times New Roman",20),bg="light yellow",fg="blue")
label2.place(x=350,y=150)

entry1=tk.Entry(system,font=("Baskerville Old Face",20),bg="white",fg="black")
entry1.place(x=720,y=155)

label3=tk.Label(system,text="Enter length of the password  ",bg="light yellow",fg="blue",font=("Times New Roman",20))
label3.place(x=350,y=250)

entry2=tk.Entry(system,font=("Baskerville Old Face",20),bg="white",fg="black")
entry2.place(x=720,y=255)

button1=tk.Button(system,text="Generate Password",font=("Baskerville Old Face",15,"bold"),bg="tomato",command=Generate_pw)
button1.place(x=250,y=350)

button2=tk.Button(system,text="Accept Password",font=("Baskerville Old Face",15,"bold"),bg="grey",fg='white',command=Accept_pw)
button2.place(x=500,y=350)

button3=tk.Button(system,text="Reset Password",font=("Baskerville Old Face",15,"bold"),bg="Yellow",command=Reset_pw)
button3.place(x=750,y=350)

button4=tk.Button(system,text="Copy Password",font=("Baskerville Old Face",15,"bold"),bg="pink",command=Copy_pw)
button4.place(x=1000,y=350)

label4=tk.Label(system,text="Generated Password",bg="light yellow",fg="blue",font=("Times New Roman",20))
label4.place(x=350,y=450)

entry3=tk.Entry(system,font=("Baskerville Old Face",20),bg="white",fg="black")
entry3.place(x=720,y=450)

label5=tk.Label(system,font=("Baskerville Old Face",20),bg="light yellow",fg="black")
label5.place(x=350,y=500)

label6=tk.Label(system,font=("Baskerville Old Face",20),bg="light yellow",fg="black")
label6.place(x=350,y=550)

system.mainloop()
