class sublista(list):
    def promedio(self):
        print("Aquí va el promedio")
        pro=sum(self)/len(self)
        return pro





milista1=sublista([1,2,3,6])
milista1.append(13)
promedio=milista1.promedio()
print(promedio)