from tkinter import *
from tkinter import filedialog
import customtkinter


# window configuration

window = Tk()

filename = 'Untitled.txt'

wi = 1000
he = 800

bes = str(wi) + 'x' + str(he)
window.geometry(bes)
window.minsize(561, 300)

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.title('Teditor')

window.configure(background='#393d47')


# Functions for Buttons

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


# Buttons

of = customtkinter.CTkButton(master=window, text='Open File', corner_radius=1, fg_color='#808699', command=OpenFile, )
of.grid(in_=window, row=0, column=1, sticky=W)

sf = customtkinter.CTkButton(master=window, text='Save File', corner_radius=1, fg_color='#808699', command=SaveFile)
sf.grid(in_=window, row=0, column=2, sticky=W)

nf = customtkinter.CTkButton(master=window, text='New File', corner_radius=1, fg_color='#808699', command=NewFile)
nf.grid(in_=window, row=0, column=3, sticky=W)

sa = customtkinter.CTkButton(master=window, text='Save As', corner_radius=1, fg_color='#808699', command=SaveFileAs)
sa.grid(in_=window, row=0, column=4, sticky=W)


text = Text(window, font='DroidSansMono 15', border=0, borderwidth=0, selectborderwidth=0, height=100, background='#22242a', foreground='#ffffff')
text.grid(in_=window, row=1, column=0, sticky='wen', columnspan=200, rowspan=1)
text.configure(spacing1=4, insertbackground='white', insertwidth=2, insertofftime=0, highlightthickness=6, highlightbackground = "#22242a", highlightcolor= "#22242a")


# Icon photo
ph = PhotoImage(file = '/usr/share/pixmaps/teditor-logo.png')
window.iconphoto(False, ph)



window.mainloop()


