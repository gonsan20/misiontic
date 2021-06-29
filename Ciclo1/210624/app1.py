from tkinter import Tk, Button, Entry

lambda

def imprimir():
    #texto.insert(index=2, string="hola pepe")
    dato = texto.get() #captura al info del entry
    texto.delete(0, 'end') #borrar entry
    print(dato)


root = Tk()
root.title("Botón")

boton = Button(root, text="hola", bg="blue violet", command= lambda : imprimir())
boton.pack()


texto = Entry(root)
texto.pack()


root.mainloop()