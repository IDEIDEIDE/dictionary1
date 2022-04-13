#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 18:16:25 2022

@author: clockshield
"""

from tkinter import *
import random
root=Tk()
root.title("lol")
root.geometry("400x400")

label_mutable = Label(root)
label_immutable = Label(root)
label_tkinter = Label(root)

dictionary ={
        "mutable" : "Mutable means changeable",   
        "Immutable" : "Immutable means unchangeable", 
        "Tkinter" : "Tkinter is a library on Python"
    
    }

def Mutable():
    label_mutable["text"] = dictionary["mutable"]
    
def Immutable():
    label_immutable["text"] = dictionary["Immutable"]
    
def Tkinter():
    label_tkinter["text"] = dictionary["Tkinter"]
    
label_mutable.place(relx = 0.5, rely = 0.3, anchor=CENTER)
btn = Button(root,text="Meaning Of Mutable",command=Mutable)
btn.place(relx = 0.5, rely = 0.2, anchor=CENTER)

label_immutable.place(relx = 0.5, rely = 0.5, anchor=CENTER)
btn1 = Button(root,text="Meaning Of Imutable",command=Immutable)
btn1.place(relx = 0.5, rely = 0.4, anchor=CENTER)

label_tkinter.place(relx = 0.5, rely = 0.7, anchor=CENTER)
btn2 = Button(root,text="Meaning Of Tkinter",command=Tkinter)
btn2.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()