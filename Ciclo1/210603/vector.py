class vector(object):
    def __init__(self, n): #Crea un 
        self.n=n
        self.V=[0]*(n+1)
        self.T="pepe"


mivector=vector(n=5)
obje_vector=vector(n=3)
#mivector.V=[1,2,3]
mivector.T="lalo"

print(mivector.V)
print(obje_vector.V)