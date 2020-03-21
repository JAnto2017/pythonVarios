#La primera funciOn calcula el cuadrado de un nUmero
def cuadrado():
    v1=int(input("Intro num1: "))
    #print('El cuadrado es',v1*v1)
    cua=v1*v1
    return cua

#La segunda funciOn calcula el producto de dos nUmeros
def producto():
    v1=int(input('Intro numX1: '))
    v2=int(input('Intro numX2: '))
    p=v1*v2
    #print('El producto es: ',p)
    return p

#La tercera funciOn imprime los datos
def salida(c,p):
    print('El cuadrado es: ')
    print(c)
    print('El producto es: ')
    print(p)

#PROGRMA PRINCIPAL
cuad = cuadrado()
prod = producto()
salida(cuad,prod)