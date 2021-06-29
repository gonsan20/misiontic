from tkinter import Tk, Label, Button, Entry, messagebox

def calcular():
    A=float(numeroA.get())
    B=float(numeroB.get())


    resultado=A+B

    E_resultado.delete(0, 'end')
    E_resultado.insert(0, str(resultado))

    """
    print(resultado)
    messagebox.showinfo("Suma", "la suma es " + str(resultado))
    """


#ventana principal
ventana = Tk()


#puntos de entrada
L_numeroA=Label(ventana, text="number A")
L_numeroA.grid(row=0, column=0, columnspan=2)
numeroA = Entry(ventana)
numeroA.grid(row=0, column=2, pady=10, padx=5)

L_numeroB=Label(ventana, text="number B")
L_numeroB.grid(row=1, column=0, columnspan=2)
numeroB = Entry(ventana)
numeroB.grid(row=1, column=2, pady=10, padx=5)

B_resultado=Button(ventana, text="Calcular", bg="blue", command=calcular)
E_resultado=Entry(ventana)
B_resultado.grid(row=2, column=2, columnspan=2)
E_resultado.grid(row=2, column=2, pady=10, padx=5)


ventana.mainloop()