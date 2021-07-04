from tkinter import ttk
from tkinter import *
from app_filtros import filtro

def filtrar():
    opcion = opciones_filtro.selection_get()
    valor=E_valor.get()
    mi_filtro=filtro(file_name='Productos.csv')
    tabla_filtrada=mi_filtro.filtrar_por(registro=opcion, valor=valor)

    mostrar_tabla(filas=len(tabla_filtrada), tabla_datos=tabla_filtrada)


def mostrar_tabla(filas, tabla_datos):
    for f in range(filas):
        for c in range (4):
            registro = Entry(tabla_datos)
            registro.grid(row=f, column=c)
            registro.insert(0,tabla_datos[f][keys[c]])



#[AN]-> Define dimensiones de la ventana
root = Tk()
root.title("filterAPP")
root.geometry('300x200')


keys =['id', 'nombre', 'cantidad', 'precio']


#[AN]-> Agregar el list box
opciones_filtro = ttk.Combobox(root, state='readonly')
opciones_filtro.grid(row=0, column=0, padx=5)
opciones_filtro['values'] = keys


#[AN]-> Crear botón de filtrado
B_filtrar=Button(root, text="Filtrar", command=filtrar)
B_filtrar.grid(row=0, column=4, padx=5)

#[AN]-> agregar label
L_valor=Label(root, text="Valor a Filtrar")
L_valor.grid(row=0, column=2)


#[AN]-> Agregar entry
E_valor=Entry(root)
E_valor.grid(row=0, column=3)


#[AN]-> Crear frame para llamar a la tabla
tabla = Frame(root)
tabla.grid(row=2, column=0)


root.mainloop()