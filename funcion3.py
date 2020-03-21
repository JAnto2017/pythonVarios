#Determina si de dos nUmeros cuAl es mayor usando las funciones
def comparador(n1,n2):
    c1=n1
    c2=n2
    if c1 > c2:
        return c1
    else:
        return c2

#MAIN
v1=int(input('Intro numero 1: '))
v2=int(input('Intro numero 2: '))
ot=comparador(v1,v2)
print('El mayor es: ',ot)