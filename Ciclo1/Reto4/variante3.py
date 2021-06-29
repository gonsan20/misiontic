# NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la clase cliente
from pruebas import pruebas_codigo_estudiante
from cliente import cliente
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""

"""Inicio espacio para programar funciones propias"""
# En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL
def determinar_cola_caja_info(cola_general):
    cola_caja=[]
    cola_info=[]
    for i in range(len(cola_general)):
        if cola_general[i].fila_interes == "caja":
            cola_caja.append(cola_general[i].nombre)
        if cola_general[i].fila_interes == "info":
            cola_info.append(cola_general[i].nombre)
    return cola_caja, cola_info


def calcular_suma_retiros_consignaciones(cola_general):
    suma_retiros = 0
    suma_consignaciones = 0
    for i in range(len(cola_general)):
        if cola_general[i].transaccion == "retirar":
            suma_retiros += cola_general[i].cantidad_retirar
        if cola_general[i].transaccion == "consignar":
            suma_consignaciones += cola_general[i].cantidad_consignar
    return suma_retiros, suma_consignaciones


def calcular_edad_minima(cola_general):
    edad_minima_retiro = 0
    edad_minima_info = 0
    edad_minima_consignacion = 0
    for i in range(len(cola_general)):
        if cola_general[i].transaccion == "retirar":
            if edad_minima_retiro == 0:
                edad_minima_retiro = cola_general[i].edad
            else:
                if cola_general[i].edad < edad_minima_retiro:
                    edad_minima_retiro = cola_general[i].edad
        if cola_general[i].transaccion == "consignar":
            if edad_minima_consignacion == 0:
                edad_minima_consignacion = cola_general[i].edad
            else:
                if cola_general[i].edad < edad_minima_consignacion:
                    edad_minima_consignacion = cola_general[i].edad
        if cola_general[i].transaccion == "ninguna":
            if edad_minima_info == 0:
                edad_minima_info = cola_general[i].edad
            else:
                if cola_general[i].edad < edad_minima_info:
                    edad_minima_info = cola_general[i].edad
    return edad_minima_retiro, edad_minima_info, edad_minima_consignacion
"""Fin espacio para programar funciones propias"""


def sede_bancaria(cola_general):
    # ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    cola_caja, cola_info = determinar_cola_caja_info(cola_general)
    suma_retiros, suma_consignaciones = calcular_suma_retiros_consignaciones(cola_general)
    edad_minima_retiro, edad_minima_info, edad_minima_consignacion = calcular_edad_minima(cola_general)
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(sede_bancaria)