from ej8 import Maquina

jugador=Maquina(saldo=4)

while True:
    input("Presione ENTER para jugar")
    jugador.jugar()
    if jugador.saldo<=0:
        break