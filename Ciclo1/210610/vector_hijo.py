from vector import vector

class altaPrecision(vector):
    def __init__(self, n):
        vector.__init__(self, n)
        self.V[0]=n
    
    def imprimeVector(self, mensaje="vector sin nombre: "):
        print("\n", mensaje)

        print(self.V[0]+1, self.n+1)

        for i in range(self.V[0]+1, self.n+1):
            print(self.V[i], end="")
        print()

    def insertar(self, d)







obj=altaPrecision(n=5)
obj.insertar(d=56)
obj.V=[3,0,0,0,5,6,4,3]

