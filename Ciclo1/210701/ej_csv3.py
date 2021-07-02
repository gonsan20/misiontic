import csv
names_columns=["Pais","Capital"]
def leer():
    with open("Tabla.csv") as csv_file:
        tabla = csv.DictReader(csv_filefieldnames=names_columns)
        for row in tabla:
            print(row)

def escribir():
    with open("Tabla.csv", 'a') as csv_file:
        tabla = csv.DictWriter(csv_file, fieldnames=names_columns)
        tabla.writerow({"Pais":"Austria", "Capital":"Viena"})






