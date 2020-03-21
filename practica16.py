#Evalúa si un entero es primo
from math import sqrt
divisor=2
es_primo=True
print("Número? ")
n=int(input())

while n<=sqrt(n) & es_primo:
    cociente = num/divisor
    if cociente*divisor==num:
        es_primo=False

    divisor=divisor+1

if (es_primo):
    print("Si es primo")
else:
    print("NO es primo")
