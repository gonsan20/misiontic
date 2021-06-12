from empleado import Empleado

class Empleado_hijo(Empleado):
     def __init__(self,area, horas, valor_hora, nombre):
         #super().__init__(self, area, horas, valor_hora)
         super().__init__(area, horas, valor_hora)
         
     def pagar(self):
         pago=super().pagar()
         print(pago)
         if self.area=='ventas':
             pago+=1000000
         print(pago)





felipe=Empleado_hijo(area='ventas', horas=160, valor_hora=30, nombre='felipe')
felipe.pagar