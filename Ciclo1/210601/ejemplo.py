n = 125

acmpio = [0] * (n + 1)

print (acmpio)
mpio = int(input("Entre código de municipio "))

while mpio != 0:

            np = int(input("Entre número de personas "))

            acmpio[mpio] = acmpio[mpio] + np

            mpio = int(input("Entre código de municipio "))

for i in range(1, n + 1):

            print("Municipio", i, "Habitantes = ", acmpio[i])