import csv

class dataClients(object):
    def __init__(self, file_name):
        self.name_file = file_name
        self.tabla=[]
        self.fieldnames=['id', 'nombre', 'cantidad', 'precio']


    def read(self):
        with open(self.name_file) as csv_file:
            datos = csv.DictReader(csv_file, fieldnames=self.fieldnames)
            for row in datos:
                self.tabla.append(row)


    def write_row(self, datos):
        with open(self.name_file, 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            if isinstance(datos, dict):
                try:
                    writer.writerow(datos)
                except:
                    return False
                else:
                    print("No tiene las keys correctas")
                    return True
            else:
                print("No es un diccionario")
                return True





mi_tabla = dataClients(file_name='Datos.csv')
dato={'id':'0001', 'nombre':'platano', 'cantidad':34, 'precio':2000}
validar=mi_tabla.write_row(dato)

print(validar)






















