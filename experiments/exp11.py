from tkinter import *

def login():
    lb1.config(text="login success : "+name_text.get())

window = Tk()

window.title("Nikal Bahar Be")

window.geometry('350x200')

name_text = StringVar()
pass_text = StringVar()

lb1 = Label(window, text="enter your UserName:", anchor=W, justify=LEFT)
lb2 = Label(window, text="enter your Password:", anchor=W, justify=LEFT)

lb1.grid(row=0,column=0)
lb2.grid(row=2,column=0)

btn_1 = Button(window,text="Enter",command=login).grid(row=3,column=0)
btn_2 = Button(window, text="Submit",command=login).grid(row=4,column=0)

Entry_1 = Entry(window,textvariable = name_text).grid(row=0,column=1)
Entry_2 = Entry(window,show="+",textvariable = pass_text).grid(row=2,column=1)

window.resizable(True,False)
window.bind(login)
window.mainloop()
