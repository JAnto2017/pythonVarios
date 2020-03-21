#DETERMIN SI UN NÚMERO ENTERO POSITIVO ES PRIMO

from math import sqrt

print("INTRO Nº ENTERO POSITIVO")
n=int(input())
print(n)

divisor = 2

while (divisor <= sqrt(n)):
    cociente = n/divisor
    print("cociente: ",cociente)
    
    if(n == cociente * divisor):
        divisor = n+1
    else:
        divisor = divisor + 1
    print("Divisor: ",divisor)    
#----------------------------------
        
if (divisor < n):
    print("No es primo")
else:
    print("Si es primo")
