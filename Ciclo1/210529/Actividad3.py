"""
Programa mostrar torre de @ dependiendo del número ingresado
"""

numero=int(input("Ingrese un número entero: "))

numero_a_mostrar=1

#Modo Novoa
while numero_a_mostrar <= numero:
    print("@"*numero_a_mostrar+"\\")
    numero_a_mostrar+=1


#Modo Compañerillo
tam = int(input('Ingrese cantidad de filas: '))

for i in range(1,tam+1):
    print(f"{'@'*i}\\")


#Modo Profesor
filas_triangulo=input("Ingrese un número entero:\t")

for i in range(1,int(filas_triangulo)+1)
print (i)