class Coche:
    def __init__(self,marca='',anio=0):
        self.marca=marca
        self.anio=anio
        print(self)

    def __str__(self):
        return "soy coche marca {marca} año {anio}".format(
            marca=self.marca,
            anio=self.anio
            )

v1 = Coche(marca='Renaul',anio=2009)
v2 = Coche(marca='Peugeot',anio=1999)
