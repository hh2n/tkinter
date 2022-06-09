from cProfile import label
from tkinter import *

root = Tk()
root.title('Hola Mundo')

root.geometry('700x500')

#label = Label(root, text='Hola mundo, primer etiqueta')
#label.pack()

l1 = Label(root, text="Mensaje de plataform")
l2 = Label(root, text="Otro mensaje")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

root.mainloop()