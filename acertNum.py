import random
numAlea = random.randint(0,50)

numUsua = int(input("Into num 1 a 49: "))

if numAlea==numUsua:
    print("Acertastes")
else:
    print("No acertastes número secreto")
    while (numAlea != numUsua):
        print("Sigue intentándolo")
        numUsua=int(input())
    print("Acertastes después del primer fallo")
    
print("Fin de programa")
