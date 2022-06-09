from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Demo Ventana")

def open():
    img = ImageTk.PhotoImage(Image.open('img/shazard.jpg'))
    top = Toplevel()
    top.title('Hola soy la ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()


btn = Button(root, text='Abrir Ventana', command=open).pack()

root.mainloop()