#segundo grado página 72
from math import *

a=float(input("Intro a: "))
b=float(input("Intro b: "))
c=float(input("Intro c: "))

#----------------------------------------
d=b*b - 4*a*c
if d>0:
    print("Raices reales y diferentes")
    x1=(-b + sqrt(d))/2/a
    x2=(-b - sqrt(d))/2/a
    print(x1)
    print(x2)
    
#----------------------------------------
if d==0:
    print("Raices reales e iguales")
    x1=-b/2/a
    x2=x1
    print(x1)
    print(x2)

#----------------------------------------
if d<0:
    print("Raices complejas y conjugadas")
    x1_parte_real=-b/2/a
    x1_parte_im=sqrt(-d)/2/a
    x2_parte_real=-b/2/a
    x2_parte_im=sqrt(-d)/2/a
    print(x1_parte_real)
    print(x1_parte_im)
    print(x2_parte_real)
    print(x2_parte_im)
