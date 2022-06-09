from glob import glob
from logging import addLevelName
from os import stat
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Hola Mundo')

img1 = ImageTk.PhotoImage(Image.open('img/fady.jpg'))
img2 = ImageTk.PhotoImage(Image.open('img/george.jpg'))
img3 = ImageTk.PhotoImage(Image.open('img/martino.jpg'))
img4 = ImageTk.PhotoImage(Image.open('img/shazard.jpg'))

lista = [img1, img2, img3, img4]

l =  Label(root, image=img1)
l.grid(row=0, column=0, columnspan=3)

def adelante(num_img):
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[num_img])
    btn_atras = Button(root, text='<--', command=lambda: atras(num_img - 1))
    btn_adelante = Button(root, text='-->', command=lambda: adelante(num_img + 1))

    if num_img == 3:
        btn_adelante = Button(root, text='---', state=DISABLED)

    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

def atras(num_img):
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[num_img])
    btn_atras = Button(root, text='<--', command=lambda: atras(num_img - 1))
    btn_adelante = Button(root, text='-->', command=lambda: adelante(num_img + 1))

    if num_img == 0:
        btn_atras = Button(root, text='---', state=DISABLED)

    l.grid(row=0, column=0, columnspan=3)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

btn_atras = Button(root, text='---', state=DISABLED)
btn_adelante = Button(root, text='-->', command=lambda: adelante(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)

root.mainloop()