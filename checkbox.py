from tkinter import *

root = Tk()
root.title("Hola Mundo: CheckBox")

root.geometry("500x500")

var = StringVar()
var.set("Chanchito Feliz")

def mostrar():
    l = Label(root, text=var.get())
    l.pack()

c = Checkbutton(root, text="Soy un CheckBox", variable=var, onvalue="SI", offvalue="Chanchito Feliz")
c.pack()

btn = Button(root, text="Click", command=mostrar)
btn.pack()

root.mainloop()