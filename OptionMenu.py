from multiprocessing.sharedctypes import Value
from tkinter import *

root = Tk()
root.title("Hola Mundo: Option Menu")
root.geometry('500x500')

def enviar():
    l = Label(root, text=value.get())
    l.pack()

lista = [
    'Cesar Espinosa',
    'Erika Nuñez',
    'Ximena Valentina',
    'Erick Santiago',
    'Paula Sofia'
]

value = StringVar()
value.set(lista[0])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()