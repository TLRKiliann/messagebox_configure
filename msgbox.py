#!/usr/bin/python3
# -*- coding:Utf-8 -*-


from tkinter import *
from message_box import *


msgbox = Tk()
msgbox.title("Click-it!")
msgbox.configure(bg='cyan')
msgbox.geometry('350x350')

def watchMessage():
	click_me()

click = Button(msgbox, text = "click me", command = watchMessage)
click.pack(padx=20, pady=150)
 
msgbox.mainloop()
