
import numpy
import math

x = float(input("ingrese la componente en x:\t"))
y = float(input("ingrese la componente en y:\t"))

angulo_radianes = math.atan(y/x)
print(f"El angulo es: {angulo_radianes}")

angulo_grados = numpy.degrees(angulo_radianes)
print(f"El angulo en grados es: {angulo_grados}")

angulo_grados_manual = 180 * angulo_radianes / 3.141516
print(f"El angulo en grados calculado manualmente es: {angulo_grados_manual}")