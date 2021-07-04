import csv



def procesar_solucion():
    fechas=[]
    proms=[]
    ranking = ["MUY BAJO", "BAJO", "MEDIO", "ALTO", "MUY ALTO"]
    with open('GOOG.csv', newline='') as File:
        reader = csv.reader(File)
        next(File, None)
        crear_archivo()
        for row in reader:
            close_value = float(row[4])
            prom_value=(float(row[2])+float(row[3]))/2
            if close_value < 1624:
                insertar_archivo(str(row[0]), ranking[0])
            elif close_value >= 1624 and close_value < 1854:
                insertar_archivo(str(row[0]), ranking[1])
            elif close_value >= 1854 and close_value < 2084:
                insertar_archivo(str(row[0]), ranking[2])
            elif close_value >= 2084 and close_value < 2314:
                insertar_archivo(str(row[0]), ranking[3])
            else:
                insertar_archivo(str(row[0]), ranking[4])
            #lleno las listas de fecha y promedio
            fechas.append(str(row[0]))
            proms.append(prom_value)
    return fechas, proms


def crear_archivo():
    with open('analisis_archivo.csv', 'w') as archivo:
        writer = csv.writer(archivo, delimiter='\t')
        writer.writerow(["Fecha", "Concepto"])

def insertar_archivo(fecha, concepto):

    with open('analisis_archivo.csv', 'a') as archivo:
        writer = csv.writer(archivo, delimiter='\t')
        writer.writerow([fecha, concepto])

def buscar_altos(fechas, proms):
    date_highest_mean=""
    highest_mean=0.0
    for i in range(len(proms)):
        if proms[i] > highest_mean:
            highest_mean=proms[i]
            date_highest_mean=fechas[i]
    return date_highest_mean, highest_mean


def buscar_bajos(fechas, proms, highest_mean):
    date_lowest_mean=""
    lowest_mean=highest_mean
    for i in range(len(proms)):
        if proms[i] < lowest_mean:
            lowest_mean=proms[i]
            date_lowest_mean=fechas[i]
    return date_lowest_mean, lowest_mean




def solucion():
    # ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    fechas, proms = procesar_solucion()
    date_highest_mean, highest_mean = buscar_altos(fechas, proms)
    date_lowest_mean, lowest_mean = buscar_bajos(fechas, proms, highest_mean)
    return date_lowest_mean, lowest_mean, date_highest_mean, highest_mean






solucion()