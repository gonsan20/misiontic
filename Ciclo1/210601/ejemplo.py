"""
ladoA=int(input("Ingrese lado 1 de rectángulo:\t"))
ladoB=int(input("Ingrese lado 2 de rectángulo:\t"))

Area= ladoB*ladoA
Perimetro1= ladoB*2 + ladoA*2
Perimetro2= (ladoB*2) + (ladoA*2)

print(Area)
print(Perimetro1)
print(Perimetro2)

"""

a = input("entre un número ")
b = input("entre otro número ")
c = int(input("entre un tercer número "))
d = int(input("entre un cuarto número "))

if  b > a:
    print(c+d, end=",")
    print(a+b)
else:
    if a == b:
        print(a, d)
    else:
        print(a, b, c, d, sep ="")