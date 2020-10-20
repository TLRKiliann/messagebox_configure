#!/usr/bin/python3
# -*- coding:Utf-8 -*-


"""
    Start this app to launch
    msg_box2.py.
"""


from tkinter import *
from msg_box2 import *


msgbox = Tk()
msgbox.title("Click-it!")
msgbox.configure(bg='cyan')
msgbox.geometry('350x350')

def watchMessage():
    """
        Click button to display
        second window or msg.
    """
    click_me()

click = Button(msgbox, text = "click me", command = watchMessage)
click.pack(padx=20, pady=150)

msgbox.mainloop()
