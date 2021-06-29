from cliente import cliente

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
    edad_minima_retiro = -1
    edad_minima_info = -1
    edad_minima_consignacion = -1
    for i in range(len(cola_general)):
        if cola_general[i].transaccion == "retirar":
            if edad_minima_retiro == -1:
                edad_minima_retiro = cola_general[i].edad
            else:
                if cola_general[i].edad < edad_minima_retiro:
                    edad_minima_retiro = cola_general[i].edad
        if cola_general[i].transaccion == "consignar":
            if edad_minima_consignacion == -1:
                edad_minima_consignacion = cola_general[i].edad
            else:
                if cola_general[i].edad < edad_minima_consignacion:
                    edad_minima_consignacion = cola_general[i].edad
        if cola_general[i].transaccion == "ninguna":
            if edad_minima_info == -1:
                edad_minima_info = cola_general[i].edad
            else:
                if cola_general[i].edad < edad_minima_info:
                    edad_minima_info = cola_general[i].edad
    return edad_minima_retiro, edad_minima_info, edad_minima_consignacion



def sede_bancaria(cola_general):
    # ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    cola_caja, cola_info = determinar_cola_caja_info(cola_general)
    suma_retiros, suma_consignaciones = calcular_suma_retiros_consignaciones(cola_general)
    edad_minima_retiro, edad_minima_info, edad_minima_consignacion = calcular_edad_minima(cola_general)
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion





cola_general = [
cliente("Matt",21,235000,"caja","retirar",100000,0),
cliente("Dan",32,658000,"caja","retirar",98000,0),
cliente("Diana",29,87000,"info","ninguna",0,0),
cliente("Carmelo",25,87000,"info","ninguna",0,0),
#cliente("Mateo",18,87000,"caja","consignar",0,15000000),
#cliente("Elisa",29,87000,"caja","consignar",0,250000),
cliente("Eliseo",45,87000,"info","ninguna",0,0)

]

print(cola_general[3].cantidad_consignar)

print("imprime info de colas")
print(determinar_cola_caja_info(cola_general))

print("imprime info de sumas de montos")
print(calcular_suma_retiros_consignaciones(cola_general))

print("imprime info de las edades")
print(calcular_edad_minima(cola_general))

clienteA = cliente("Matt",21,235000,"caja","retirar",100000,0)

print(clienteA.nombre)

#sede_bancaria(cola_general)