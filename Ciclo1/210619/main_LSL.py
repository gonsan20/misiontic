from ListasLigadas import LSL

lista1 = LSL()

for i in range(1,5):
    d = int(input("Entre dato: "))
    y = lista1.buscarDondeInsertar(d=d)
    lista1.insertar(d=d, y=y)
    print(i)
lista1.recorrerLista()

for i in range(2):
    d = int(input("Entre dato a insertar: "))
    lista1.agregarDato(d=d)
    print(i)

lista1.recorrerLista()