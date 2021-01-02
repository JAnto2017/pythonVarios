class Coche:
    def __init__(self,marca='',anio=0):
        self.marca = marca
        self.anio = anio
        print(self)

    def __str__(self):
        return "Soy un coche:\n{marca}\n{anio}".format (
            marca = self.marca,
            anio = self.anio
        )
#-------------------------------------------------------------------
class Marca:
    def __init__(self,nombre=''):
        self.nombre = nombre

    def __str_(self):
        if self.nombre == 'Peugeot':
            eslogan = 'La marca del león'
        elif self.nombre == 'Renaul':
            eslogan = 'Passion for life'
        else:
            eslogan = 'Ninguno'
        return '{marca}: {eslogan}'.format(
            marca = self.nombre,
            eslogan = eslogan
        )
#-------------------------------------------------------------------
class Anio:
    def __init__(self,anio=0):
        self.anio = anio

    def __str__(self):
        return 'Anio: {anio}'.format(
            anio = self.anio
        )
#------------------------------------------------------------------
v1 = Coche(marca=Marca('Peugeot'), anio=Anio(1999))
v2 = Coche(marca=Marca('Renault'), anio=Anio(2009))
