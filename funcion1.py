#Uso de funciones
def pedirDatos():
    v1=int(input("Intro num1: "))
    v2=int(input("Intro num2: "))
    sum=v1+v2
    print('La suma es: ',sum)

def separar():
    print("+++++++++++++++++++++++++++++")

#PROGRAMA PRINCIPAL
for x in range(3):
    pedirDatos()
    separar()