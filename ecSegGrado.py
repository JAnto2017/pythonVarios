#EC. SEGUNDO GRADO
#INICIO

from math import *

a=float(input("Intro a: "))
b=float(input("Intro b: "))
c=float(input("Intro c: "))

#calculo del discriminante
d= b*b - 4*a*c
#print(d)

if(d > 0):
    print("Raices reales distintas")
    x1=(-b + sqrt(d))/2/a
    x2=(-b - sqrt(d))/2/a
    print(x1)
    print(x2)
#-------------------------

if(d == 0):
    print("Raices reales iguales")
    x1= -b /2/a
    x2= x1
    print(x1)
    print(x2)
#-------------------------

if(d < 0):
    print("Raices complejas")
    x1_re = -b/2/a
    x1_im = sqrt(-d)/2/a

    x2_re = -b/2/a
    x2_im = sqrt(-d)/2/a

    print(x1_re)
    print(x1_im)
#.......................
