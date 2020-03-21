#Algoritmo Calculadora
from math import log

bandera=False

x=float(input("Intro num X: "))
y=float(input("Intro num Y: "))
print("Selecciona opción:\n")
#menu para opción
print("1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("4) Dividir")
print("5) Potencia")
print("6) Logaritmo")
opcion=int(input("Intro opción: "))

#---------------------------------------
if (opcion==1):
    z=x+y
    print(x,"+",y)
elif (opcion==2):
    z=x-y
    print(x,"-",y)
elif (opcion==3):
    z=x*y
    print(x," X ",y)
elif (opcion==4 and y !=0):
    z=x/y
    print(x,"/",y)
elif (opcion==4 and y==0):
    print("Denominador = 0")
    print("NO se puede dividir")
    bandera=True
elif (opcion==5):
    z=pow(x,y)
    print(x,"^",y)
elif (opcion==6 and x>0):
    z=log(x)
    print("Log de",x)
elif (opcion==6 and x<=0):
    print("Valor de x <= 0")
    print("NO se puede calcular el logaritmo")
    bandera=True
else:
    print("Opción desconocida")

if(opcion<7 and bandera==False):
    print("Resultado =",z)
