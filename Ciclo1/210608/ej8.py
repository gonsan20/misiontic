"""
clase para gestionar una máquina tragamonedas
"""
import random as rnd

class Maquina(object):
    def __init__(self,saldo):
        self.saldo=saldo
    
    def jugar(self):
        simbolos=['$','7','#','1','3']
        simbolos_juego=list() #-> Creamos una lista
        for i in range (3): #-> Generar los 3 símbolos del juego
            aleatorio=rnd.randint(0,len(simbolos)-1)
            simbolos_juego.append(simbolos[aleatorio])
        
        print(simbolos_juego)
        print(f"|\t{simbolos_juego[0]}\t|\t{simbolos_juego[1]}\t|\t{simbolos_juego[2]}\t|")
        self.validar(jugada=simbolos_juego)
        print(f"\nSu saldo es {self.saldo}")

    def validar(self,jugada): #-> jugada trae los 3 símbolos generados en el juego
        if jugada[0]==jugada[1] and jugada[0]==jugada[2]:
            print("Habeís Ganado")
            self.saldo+=10
        else:
            print("Habeís Perdido")
            self.saldo-=2
        pass



mi_maquina=Maquina(saldo=45)
mi_maquina.jugar()