lista=[-3,0,-100, 50, 89, 9, 1, 4, 45]

mayor=lista[0]
r=0
p=0
#Mecanismo 2 de recorrer una lista
for posicion in lista: 
    numero = posicion
    if numero > mayor:
        mayor=numero
        p=r
    r+=1

print(f"el numero mayor {mayor} y se encuentra en la posición {p}")