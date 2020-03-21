cant1=0
cant2=0
cant3=0
#-----------------------------------------------------
n=int(input("Cantidad de triángulos? "))
for x in range(n):
    lado1=int(input("lado 1? "))
    lado2=int(input("lado 2? "))
    lado3=int(input("lado 3? "))
    if lado1==lado2 and lado1==lado3:
        print("Triángulo EQUI-LATERO")
        cant1=cant1+1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Triángulo ISÓS-CELES")
            cant2=cant2+1
        else:
            print("Triángulo ESCA-LENO")
            cant3=cant3+1

print("Total triángulos EQUILÁTEROS: ")
print(cant1)
print("Total triángulos ISÓSCELES: ")
print(cant2)
print("Total triángulos ESCALENOS: ")
print(cant3)
