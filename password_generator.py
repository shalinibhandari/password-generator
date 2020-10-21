import tkinter
from tkinter import *
import random
import pyperclip

def low():
    entry.delete(0,END)
    length=val1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    if(var.get()==1):
        for i in range(0,length):
            password=password+random.choice(lower)
    elif(var.get()==2):
        for i in range(0,length):
            password=password+random.choice(upper)
    elif(var.get()==3):
        for i in range(0,length):
            password=password+random.choice(digits)
    return password
        

def generate():
    password1=low()
    entry.insert(10,password1)
    
root=Tk()
root.title("password generator")
val1=IntVar
var=IntVar()
root.config(background="black")
root.geometry("600x200")
label=Label(root,text="Password Generator",bg="black",fg="cyan",font=("verdence",20))
label.place(x=168,y=2)

def copy():
    copy_password=entry.get()
    pyperclip.copy(copy_password)

#for password generate
label3=Label(root,text="Password",font=("verdence",13),fg="white",bg="black")
label3.place(x=100,y=40)
entry=Entry(root,font=("verdence",16),width=18)
entry.place(x=180,y=40)
button=Button(root,text="Generate",command=generate)
button.place(x=440,y=40)
#for length
label=Label(root,text="Length   ",font=("verdence",13),bg="black",fg="white")
label.place(x=100,y=70)
entry1=Entry(root,font=("verdence",16),textvariable=val1,width=18)
entry1.place(x=180,y=70)

#for strength of password
label2=Label(root,text="Strength ",font=("verdence",13),bg="black",fg="white")
label2.place(x=100,y=110)
rad1=Radiobutton(root,text="Low   ",variable=var,value=1)
rad1.place(x=180,y=110)
rad2=Radiobutton(root,text="Medium",variable=var,value=2)
rad2.place(x=245,y=110)
rad3=Radiobutton(root,text="  High     ",variable=var,value=3)
rad3.place(x=324,y=110)
#for coping the password
button2=Button(root,text="   Copy   ",command=copy,)
button2.place(x=440,y=70)



