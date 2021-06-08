from vector import vector
import random as rnd

N=int(input('Ingrese el tamaño del vector:\t'))
objeto_vector=vector(n=N) #se crea el objeto de la clase vector
for i in range(N):
    numero_aleatorio=rnd.randint(0,99)
    objeto_vector.insertar(d=numero_aleatorio)

print(objeto_vector.V)
mayor=objeto_vector.mayor()
print(f"El número mayor es:\t{objeto_vector.V[mayor]}")