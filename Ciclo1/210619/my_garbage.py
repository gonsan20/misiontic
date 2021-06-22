from util import palabras, grafico

palabra_secreta = "pepa"

print (palabra_secreta)

cadena=list(palabra_secreta)
longitud= len(palabra_secreta) *2 + 1

print(cadena)
print (longitud)

print(cadena[0])
print(cadena[1])
print(cadena[2])
print(cadena[3])

"""
cadena.insert(1,0)
cadena.insert(3,0)
cadena.insert(5,0)
cadena.insert(7,0)
print(cadena)
"""



#-> para funcion de crear cadena
for i in range (longitud):
    if i % 2 == 0:
        cadena.insert(i, 0)
print(cadena)

letra="p"

for j in range (1,longitud):
    if j % 2 == 1:
        if letra == cadena[j]:
            cadena[j+1]=1
            cadena[0]+=2
print(cadena)



dibujo = grafico()
print (dibujo.get_grafico(6))