lista=['juan','jesus','jose','maria','paola','erika']

#Mecanismo 1 de recorrer una lista
r=len(lista)
for pos in range(r):
    nombre=lista[pos]
    print("A - El nombre es %s"%(nombre))

#Mecanismo 2 de recorrer una lista
for nombreB in lista: 
    print("B - El nombre es %s"%(nombreB))

