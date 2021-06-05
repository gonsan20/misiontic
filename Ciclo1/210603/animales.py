class Aves(object):
    def __init__(self, especie, pais):
        self.especie=especie
        self.pais=pais

    def volar(self):
        return True
    
    def poner_huevos(self, cantidad):
        print(f"los {self.especie} ponen {cantidad} huevoz a la vez")

    #class Peces(object)



aguila=Aves(especie='Aguilas', pais='USA')
colibri=Aves(especie='Colibris', pais='Colombia')
print(aguila.pais)
print(colibri.pais)

aguila.volar()
