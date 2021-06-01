"""
programa para calcular los números pares
El usuario ingresa el límite superior para encontrar los pares
"""

numero=int(input("Ingrese un número entero: "))

numero_a_mostrar=1

while numero_a_mostrar <= numero:
    if not (numero_a_mostrar%2):
        print(numero_a_mostrar)
    numero_a_mostrar+=1