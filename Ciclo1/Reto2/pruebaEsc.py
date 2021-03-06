import numpy as np

# NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
# LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

# En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""


# PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES
def calc_sum_diagonal_principal(A, fila, columna):
    suma = 0
    auxCol = 0
    for i in range(0, fila):
        for j in range(auxCol, columna):
            suma += A[i, j]
            auxCol = j + 1
            break
    return suma


def calc_prod_diagonal_secundaria(A, fila, columna):
    producto = 1
    auxCol = columna - 1
    for i in range(0, fila):
        for j in range(auxCol, -1, -1):
            producto *= A[i, j]
            auxCol = j - 1
            break
    return producto


"""Fin espacio para programar funciones propias"""


def solucion(A):
    """
    En esta función deberás programar tu solución.
    Explicación del parámetro que recibe:
    - A: Es una matriz cuadrada de números enteros aleatoria (NO TE DEBES PREOCUPAR POR LLENARLA, YA LO ESTÁ),
        para indexar un elemento en la fila i, columna j se hace así:
        A[i,j] o A[i][j], como te sientas más cómod@.
        El orden de la matriz lo puedes calcular así: n = A.shape[0]

    Explicación de lo que debe retornar:
    -sum_diagonal_principal: Suma de los elementos de la diagonal principal, es de tipo float o entero (Elige el tipo que quieras).
    -prod_diagonal_secundaria: Producto de los elementos de la diagonal secundaria, es de tipo float o entero (Elige el tipo que quieras)
    -resultado2_mod_resultado1:  Módulo entre prod_diagonal_secundaria y sum_diagonal_principal, es de tipo float o entero (Elige el tipo que quieras)
    """
    fila = A.shape[0]
    columna = A.shape[1]

    if fila == columna:
        sum_diagonal_principal = calc_sum_diagonal_principal(A, fila, columna)
        prod_diagonal_secundaria = calc_prod_diagonal_secundaria(A, fila, columna)
        resultado2_mod_resultado1 = prod_diagonal_secundaria % sum_diagonal_principal
    else:
        sum_diagonal_principal = 0
        prod_diagonal_secundaria = 0
        resultado2_mod_resultado1 = 0

    return sum_diagonal_principal, prod_diagonal_secundaria, resultado2_mod_resultado1


"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
# NO MODIFICAR
matriz_entrada = np.array([[73, 13, 6, 1, 29],
                           [28, 72, 76, 86, 48],
                           [94, 18, 32, 24, 33],
                           [63, 11, 16, 69, 40],
                           [38, 20, 45, 78, 61]])
dp_correcto = 307
ds_correcto = 33359744
ds_mod_dp_correcto = 203

dp_estudiante = solucion(matriz_entrada)[0]
ds_estudiante = solucion(matriz_entrada)[1]
ds_mod_dp_estudiante = solucion(matriz_entrada)[2]

print("MATRIZ ENTREGADA:\n", matriz_entrada, "\n")
print(f"""===SALIDA ESPERADA===
        Suma de los elementos de la diagonal principal = {dp_correcto}
        Producto de los elementos de la diagonal secundaria = {ds_correcto}
        {ds_correcto} mod {dp_correcto} = {ds_mod_dp_correcto}""")

print(f"""===TU SALIDA===
        Suma de los elementos de la diagonal principal = {dp_estudiante}
        Producto de los elementos de la diagonal secundaria = {ds_estudiante}
        {ds_estudiante} mod {dp_estudiante} = {ds_mod_dp_estudiante}\n""")

if dp_correcto == dp_estudiante and ds_correcto == ds_estudiante and ds_mod_dp_correcto == ds_mod_dp_estudiante:
    print("Todo se ve correcto, ¡Procede a calificar tu código!")
else:
    print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")
