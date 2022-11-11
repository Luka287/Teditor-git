from tkinter import *
from tkinter import filedialog
import os

filename = None
window = Tk()
wi = 500
he = 500
window.minsize(wi, he)

text = Text(window, font='DroidSansMono 13', border=0, borderwidth=0, background='#ffffff', width=wi, selectborderwidth=0, height=39, highlightthickness=0)

text.pack()

def NewFile():
    global filename
    text.delete(0.0, END)
    g = filedialog.asksaveasfilename()
    filename = g

def OpenFile():
    global filename
    global text
    g = filedialog.askopenfile(mode='r')
    filename = g.name
    t = g.read()
    text.delete(0.0, END)
    text.insert(0.0, t)


def SaveFile():
    global filename
    global text
    t = text.get(0.0, END) 
    f = open(filename, "w")
    f.write(t)
    f.close()

def SaveFileAs():
    global filename
    global text
    g = filedialog.asksaveasfile(mode='w')

    

bu = Button(text='open', command=OpenFile)
bu.pack(in_=window, side=LEFT)

nu = Button(text='save', command=SaveFile)
nu.pack(in_=window, side=LEFT)

vu = Button(text='new', command=NewFile)
vu.pack(in_=window, side=LEFT)

ku = Button(text='save as', command=SaveFileAs)
ku.pack(in_=window, side=LEFT)


window.mainloop()