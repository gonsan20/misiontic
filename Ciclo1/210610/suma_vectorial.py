class sumaVectorial(list):
    def __add__(self, x):
        suma=[]
        for i in range(len(self)):
            suma.append(self[i]+x[i])
        return suma




v1=sumaVectorial([1,4,10])
v2=sumaVectorial([0,-2,-10])

print(v1+v2)