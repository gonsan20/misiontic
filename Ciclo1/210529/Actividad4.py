"""
Programa mostrar torre de @ dependiendo del número ingresado
"""

limite=int(input("Ingrese la cantidad de números que desea ingresar: "))
digitos=["primer","segundo","tercer"]
todos_los_numeros=list()
numero_anterior=0

for i in range(limite):
    numero_ingresado=int(input("Ingrese el %s numero: "%(digitos[i])))

    if numero_ingresado>numero_anterior: #en la primera iteración hace un proceso
        todos_los_numeros.append(numero_ingresado) #agregamos número válido a la lista


