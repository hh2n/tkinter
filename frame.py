from tkinter import *

root = Tk()
root.title("Hola Mundo")
#root.geometry('700x500')

#frame = LabelFrame(root, text="Login", padx=20, pady=20, borderwidth=10)
frame = Frame(root, padx=20, pady=20, borderwidth=10)
frame.pack(padx=50, pady=50)

label = Label(frame, text="Inicia Sesion, Ingresando tu datos: ")
btn = Button(frame, text="Salir", command=root.quit)

label.pack()
btn.pack()


root.mainloop()