from tkinter import *

root = Tk()
root.title('Hola Mundo')

r = IntVar()
r.set('2')

CHANCHITOS = [
    ('Feliz','Feliz'),
    ('Triste','Triste'),
    ('Amargado','Amargado'),
    ('Wolfgang','Wolfgang')
]

##Radiobutton(root, text='Opcion 1', variable=r, value=1).pack()
##Radiobutton(root, text='Opcion 2', variable=r, value=2).pack()
chanchito = StringVar()
chanchito.set('Wolfgang')

for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()

l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()