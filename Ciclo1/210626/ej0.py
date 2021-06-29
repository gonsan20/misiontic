from tkinter import Tk, Label, Button

def click():
    etiqueta.configure(text="hola", bg="blue")



ventana = Tk()
ventana.title("")
ventana.resizable(True,True)
ventana.iconbitmap("monkey.ico")


etiqueta = Label(ventana, text="Hola", bg="Steelblue2")
etiqueta.pack()

boton = Button(ventana, text="Imprimir", bg="coral3", height="15", width=15, command=click())
boton.pack(padx=0, pady=20)


ventana.mainloop()