def comparar(Numero_A, Numero_B):
    if Numero_A>Numero_B:
        print(f"el mayor es el {Numero_A}")
    elif Numero_A==Numero_B:
        print(f"{Numero_A} es igual a {Numero_B}")
    else:
        print(f"el mayor es el {Numero_B}")


"""
Función para obtener promedio de una lista numérica
"""
def calcularPromedio(datos):
    contador=0
    suma=0
    for valor in datos:
        suma+=valor
        contador+=1

    calc_promedio=suma/contador
    return calc_promedio





"""
Sección de ejecución
"""
print(comparar(4,4))
resultado=calcularPromedio(datos=[1,2,3,2])
print(resultado)