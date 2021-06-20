import numpy as np


matriz_entrada = np.array([[73, 13, 6, 1, 29],
                           [28, 72, 76, 86, 48],
                           [94, 18, 32, 24, 33],
                           [63, 11, 16, 69, 40],
                           [38, 20, 45, 78, 61]])
dp_correcto = 307
ds_correcto = 33359744
ds_mod_dp_correcto = 203


print (matriz_entrada[0,4])
print (matriz_entrada[1,3])
print (matriz_entrada[2,2])
print (matriz_entrada[3,1])
print (matriz_entrada[4,0])
print("------------viendoShape")
print (matriz_entrada.shape[3])

print("--------------\n")
print(type(matriz_entrada.shape[0]))
fila = int(str(matriz_entrada.shape)[1:2])
print(fila)

columna = int(str(matriz_entrada.shape)[4:5])
print(columna)
print("--------------\n")
producto=1

auxCol=columna-1
for i in range(0, fila):
    for j in range(auxCol, -1, -1):
        print(matriz_entrada[i, j])
        producto*=matriz_entrada[i, j]
        auxCol=j-1
        #break
print(f"---------\nproducto es:\t{producto}")



print("\n---------\nejemplo suma\n")

print (matriz_entrada[0,0])
print (matriz_entrada[1,1])
print (matriz_entrada[2,2])
print (matriz_entrada[3,3])
print (matriz_entrada[4,4])

print("\n---------\nResolver suma\n")
suma=0
auxCol=0
for i in range(0, fila):
    for j in range(auxCol, columna):
        print(matriz_entrada[i, j])
        suma+=matriz_entrada[i, j]
        auxCol = j + 1
        #break
print(f"---------\nsuma es:\t{suma}")
