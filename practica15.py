#Determina si un número entero positivo es primo
from math import sqrt

print("Intro número entero positivo? ")
n=int(input())
divisor=2

while (divisor <= sqrt(n)):
    cociente=n/divisor
    if (n==cociente * divisor):
        divisor=n+1
    else:
        divisor = divisor + 1


if (divisor>=n):
    print("No es primo")
else:
    print("Si es primo")
