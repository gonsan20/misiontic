class Empleado(object):
    def __init__(self,area, horas, valor_hora):
        self.datos={'area':area,'horas':horas}
        self.valor_hora=valor_hora
        
    def pagar(self):
        N_horas=self.datos['horas']
        valor_pago=N_horas*self.valor_hora

        return valor_pago



"""
juan=Empleado(area='ventas', horas=100, valor_hora=60000)
pago=juan.pagar()
print(f"El pago de Juan es {pago}")
"""