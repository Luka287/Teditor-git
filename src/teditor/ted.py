from tkinter import *
from tkinter import filedialog


window = Tk()

filename = None

wi = 1000
he = 800

bes = str(wi) + 'x' +str(he)
window.geometry(bes)
window.minsize(300, 300)

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.title('Teditor')



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
bu.grid(in_=window, row=0, column=1, sticky=W)

nu = Button(text='save', command=SaveFile)
nu.grid(in_=window, row=0, column=2, sticky=W)

vu = Button(text='new', command=NewFile)
vu.grid(in_=window, row=0, column=3, sticky=W)

ku = Button(text='save as', command=SaveFileAs)
ku.grid(in_=window, row=0, column=4, sticky=W)

text = Text(window, font='DroidSansMono 13', border=0, borderwidth=0, background='#ffffff', selectborderwidth=0, highlightthickness=0, height=100)
text.grid(in_=window, row=1, column=0, sticky='wen', columnspan=200, rowspan=1)


window.mainloop()
