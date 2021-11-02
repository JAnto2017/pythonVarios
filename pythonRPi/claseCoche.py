
class Coche:
    #constructor
    def __init__(self, marca='', anio=0):
        self.marca = marca
        self.anio = anio
        print(self)
    
    def __str__(self):
        return "Soy un coche de la marca {marca} año {anio}".format(
            marca = self.marca,
            anio = self.anio
        )

v1 = Coche(marca='Renault Clio',anio=2009)
v2 = Coche(marca='Peugeot 106',anio=1999)
print(v1)
#print(v2)