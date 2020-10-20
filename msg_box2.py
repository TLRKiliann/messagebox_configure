#!/usr/bin/python3
# -*- encoding:Utf-8 -*-

"""
    Don't use this app !!!
    It's an extension of
    msgbox.py
"""


from tkinter import *


def click_me():
    msg = Tk()
    msg.title("MESSAGEBOX")
    msg.configure(bg='grey30')
    msg.geometry('300x200')

    labelbox=Label(msg, text="Do you want to quit ?",
        font=('Times', 18, 'bold'), fg='cyan', bg='grey30')
    labelbox.pack(padx=30, pady=50)

    buttOnebox=Button(msg, text="YES", width=7, bd=3, 
        fg='cyan', bg='RoyalBlue4', activeforeground='white',
        activebackground='dark turquoise',
        highlightbackground='cyan', command=quit)
    buttOnebox.pack(side=LEFT, expand=YES)

    buttTwobox=Button(msg, text="NO", width=7, bd=3,
        fg='cyan', bg='RoyalBlue4', activeforeground='red',
        activebackground='orange',
        highlightbackground='red')
    buttTwobox.pack(side=LEFT, expand=YES)
