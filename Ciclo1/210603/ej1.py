from vector import vector

N=int(input('Ingrese el tamaño del vector:\t'))
if N>0 and N<=5:
    objeto_vector=vector(n=N) #se crea el objeto de la clase vector
    for i in range(N):
        elemento=int(input(f"Ingrese el valor {i}:\t"))
        objeto_vector.insertar(d=elemento)
    
    print(objeto_vector.V)
    mayor=objeto_vector.mayor()
    print(f"El número mayor es:\t{objeto_vector.V[mayor]}")

else:
    print("El valor debe estár entre 1 y 5")
