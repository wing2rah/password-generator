from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import string
import random
import time
root=Tk()
root['bg']="#b1fcef"
root.geometry("280x100")
root.resizable(False,False)

characters = string.ascii_letters + string.punctuation+ string.digits

password = ""
password_length = random.randint(6,15)

for x in range(password_length):
    char = random.choice(characters)
    password = password + char

def gnr():
    global password
    val.set(password)
def save():
    fin=open(r"C:\Users\ACER\Desktop\rahul shah\password\password.txt","a")
    passw=val.get()
    ans=simpledialog.askstring("enter","this password is for (e.g google)...")
    rec=ans+"---->"+passw
    fin.write(rec)
    fin.write('\n')
    fin.write('\n')
    fin.close()
    messagebox.showinfo("from rahul","successfully saved the password ")
val=StringVar()
intp=Entry(root,textvariable=val,bd=5,width=45,justify=CENTER,background="#a6c4e0").grid(row=0,column=0,pady=5,columnspan=2)
btn=Button(root,text="generate",height=2,bd=5,width=10,background="#97e8f0",foreground="black",activebackground="#485acf",activeforeground="#c94f98",command=gnr).grid(column=0,row=1)
btn1=Button(root,text="save",height=2,bd=5,width=10,background="#97e8f0",foreground="black",activebackground="#485acf",activeforeground="#c94f98",command=save).grid(column=1,row=1,pady=10)
root.mainloop()
