#!/usr/bin/python3
# -*- coding:Utf-8 -*-


from tkinter import *

 
def click_me():
    message = Tk()
    message.title("MESSAGEBOX")
    message.configure(bg='grey30')
    message.geometry('300x200')

    labelbox=Label(message, text="Do you want to quit ?",
        font=('Times', 18, 'bold'), fg='cyan', bg='grey30')
    labelbox.pack(padx=30, pady=50)

    buttOnebox=Button(message, text="YES", width=7, bd=3, 
        fg='cyan', bg='RoyalBlue4', activeforeground='white',
        activebackground='dark turquoise',
        highlightbackground='cyan', command=quit)
    buttOnebox.pack(side=LEFT, expand=YES)

    buttTwobox=Button(message, text="NO", width=7, bd=3,
        fg='cyan', bg='RoyalBlue4', activeforeground='red',
        activebackground='orange',
        highlightbackground='red')
    buttTwobox.pack(side=LEFT, expand=YES)
