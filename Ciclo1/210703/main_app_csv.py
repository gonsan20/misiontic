from data_csv import dataClients

mi_tabla = dataClients(file_name='Datos.csv')

dato = {'id':'0002', 'nombre':'uvas', 'cantidad':100, 'precio':120000}

validar = mi_tabla.write_rwo(dato)

print(validar)

#mi_tabla.read()