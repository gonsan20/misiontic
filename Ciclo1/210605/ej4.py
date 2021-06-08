#Crea circulos
class circulo(object):
    def __init__(self,radio):
        self.r=radio
        self.pi=3.1416

    def calcularArea(self):
        area=self.pi*self.r**2
        return area

    def calcularPerimetro(self):
        perimetro=2*self.pi*self.r
        return perimetro

    def calcularEcuacion(self):
        ecuacion=f"xº+yº={self.r}º"
        return ecuacion
