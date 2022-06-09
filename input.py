from cgitb import text
from tkinter import *

root = Tk()
root.title('Hola Mundo')
root.geometry('700x500')

e = Entry(root, width=30)
e.pack()
e.insert(0, "Ingresa Texto ... ")

def click2():
    texto = e.get()
    textVariable.set(texto)
    #l = Label(root, text=texto)
    #l.pack()
    e.delete(0, END)
    #label.configure(text=texto)

btn = Button(root, text='Click', command=click2)
btn.pack()

textVariable = StringVar()

label = Label(root, textvariable=textVariable)
label.pack()
root.mainloop()

