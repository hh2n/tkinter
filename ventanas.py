from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Demo Ventana")

#Solucion 1
""" def open():
    img = ImageTk.PhotoImage(Image.open('img/shazard.jpg'))
    top = Toplevel()
    top.title('Hola soy la ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop() """

# Solucion 2
""" def open():
    global img
    img = ImageTk.PhotoImage(Image.open('img/shazard.jpg'))
    top = Toplevel()
    top.title('Hola soy la ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack() """

# Solucion 3
def open(img):
    top = Toplevel()
    top.title('Hola soy la ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()

img = ImageTk.PhotoImage(Image.open('img/shazard.jpg'))
btn = Button(root, text='Abrir Ventana', command=lambda: open(img)).pack()

root.mainloop()