from ej4 import circulo


circulo_1=circulo(radio=2)
circulo_2=circulo(radio=180)

respuesta=circulo_1.calcularArea()

print(f"Área del círulo 1:\t{respuesta}")
print(f"Área del círulo 2:\t{circulo_2.calcularArea()}")