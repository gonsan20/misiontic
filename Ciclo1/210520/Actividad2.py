import random

numeroX=random.randint(1,20) #se genera el numero aleatorio

#Intento1
perdiste = True

for intento in range(1,10):
    numeroUsuario=int(input("Intento %s\nIngrese un numero de 1 a 20 -> "%(intento)))
    if (numeroUsuario== numeroX):
        print("Felicitaciones ha ganado")
        perdiste= False
        break
    elif (numeroUsuario > numeroX):
        print("El %s es mayor que el numero a adivinar"%(numeroUsuario))
    else:
        print("El %s es menor que el numero a adivinar"%(numeroUsuario))

if perdiste:
    print("No eres bueno en esto")