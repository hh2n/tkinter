from tkinter import *

root = Tk()

root.title('Hola Mundo')
root.geometry('700x500')

l = Label(root, text="Hola de nuevo !!!!")
def click():
    l.pack()


btn = Button(root, text="Ejemplo Button Ckick", command=click, fg="red", bg="blue")
btn.pack()

root.mainloop()