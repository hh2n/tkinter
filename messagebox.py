from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hola Mundo")

def click():
    messagebox.showinfo('Info: ', 'Mensaje Informativo')
    
def clickWar():
    messagebox.showwarning('Alerta: ', 'Mensaje de warning !!! ')

def clickErr():
    messagebox.showerror('Peligro: ', 'Mensaje de Error')

def clickYesNo():
    respuesta = messagebox.askquestion('Continuar: ', 'Desea continuar con la operacion?')
    if respuesta == 'yes':
        messagebox.showinfo('Respuesta: ', 'OK continuamos !!!')
    else:
        messagebox.showwarning('Respuesta: ', 'Cancelando procesos .... ')

def clickConfirm():
    respuesta  = messagebox.askokcancel('Cancelar', 'Seguro de continuar con esta acción?')
    if respuesta:
        messagebox.showinfo('Confirmado', 'La respuestas fue OK')
    else:
        messagebox.showerror('Cancelado', 'La resuesta fue Cancelar')


btnInfo = Button(root, text=' :: Info :: ', command=click)
btnInfo.pack()

btnWarning = Button(root, text=' :: Warning :: ', command=clickWar)
btnWarning.pack()

btnError = Button(root, text=' :: Error :: ', command=clickErr)
btnError.pack()

btnYesNo = Button(root, text=' :: Si o No :: ', command=clickYesNo)
btnYesNo.pack()

btnConfirm = Button(root, text=' :: Confirmar :: ', command=clickConfirm)
btnConfirm.pack()

root.mainloop()