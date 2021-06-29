from tkinter import Tk, Label

#Ventana root
ventana = Tk()
ventana.title("titulo")

#Crear etiqueta
etiqueta = Label(ventana,text="hola mundo").pack()


ventana.mainloop()

