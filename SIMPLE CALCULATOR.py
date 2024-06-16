import tkinter as tk

value=" "
def display(key):
    global value
    value+=key
    label1.config(text=value)
    
def result():
    global value
    result=""
    if value!="":
        try:
            result=str(eval(value))
        except:
            result="Error"
            value=""
        label1.config(text=result)

def clear():
    global value
    value=""
    label1.config(text=value)


system=tk.Tk()
system.title("Simple Calculator")
system.configure(bg='white')

label1=tk.Label(system,width=24,height=3,font=("Times New Roman",20,"bold"),bg='white',fg='black')
label1.grid(row=0,column=0,columnspan=5)

buttons=['C','(',')','/','7','8','9','*','4','5','6','+','1','2','3','-','.','0','%','=']
row_val=1
col_val=0

for button in buttons:
    action=lambda x=button:display(x) if x not in ['=','C'] else result() if x =='=' else clear()
    if button=='C':
        tk.Button(system,text=button,bg='blue',width=5,height=1,font=('Arial',23),command=action).grid(row=row_val,column=col_val)
        col_val+=1
    elif button=="=":
        tk.Button(system,text=button,bg='yellow',width=5,height=1,font=('Arial',23),command=action).grid(row=row_val,column=col_val)
        col_val+=1
    else:
        tk.Button(system,text=button,bg='black',width=5,height=1,fg='white',font=('Arial',23),command=action).grid(row=row_val,column=col_val)
        col_val+=1
        if col_val>3:
            col_val=0
            row_val+=1

system.mainloop()

    
    
