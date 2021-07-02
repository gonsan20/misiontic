import csv

with open('paises.csv',newline='') as csv_file:
    tabla = csv.reader(csv_file)


    for row in tabla:
        print(row[0])
