class listaHija(list):
    def promedio(self):
        print("se imprime el promedio")

class listaHija2(list):
    def append(self):
        print("este método no es válido")



a=listaHija()
a.append(4)
a.promedio
print(a)
print(type(a))


a=listaHija()
a.append(4)
a.promedio
print(a)
print(type(a))




lista=[1,3]
lista.append(100)

milista=listaHija2
milista.append()

print(lista, milista)