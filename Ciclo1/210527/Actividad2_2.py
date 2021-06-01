dictionay={'1':'Elene', '3':'Algo'}

#Mecanismo 1 de recorrer una diccionario
r=len(dictionay)
for pos in range(r):
    nombre=dictionay[pos]
    print("A - El nombre es %s"%(nombre))

#Mecanismo 2 de recorrer una diccionario
for nombreB in dictionay: 
    print("B - El nombre es %s"%(nombreB))