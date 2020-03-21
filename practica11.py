def mayor(v1,v2,v3):
    print("El mayor de los tres")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)
def cargar():
    v1=int(input("Intro v1: "))
    v2=int(input("Intro v2: "))
    v3=int(input("Intro v3: "))
    mayor(v1,v2,v3)

# Programa Principal
"programa arranca en el bloque principal"

cargar()
