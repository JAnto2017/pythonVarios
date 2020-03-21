#Diccionario - utiliza una clave para acceder a un valor
#Programa que almacena 5 articulos
#utiliza como clave el nombre de producto
#y como valor el precio del mismo
#------------------------ Cargar datos
def cargar():
    prod={}
    for x in range(5):
        nom=input("Nombre producto: ")
        pre=int(input("Precio: "))
        prod[nom]=pre
    return prod
#................ imprime productos
def imprimir(prod):
    print("Articulos")
    for nom in prod:
        print(nom,prod[nom])    
#................ imprime productos>100
def imp_mayor1000(prod):
    print("Art. precio > 100: ")
    for nom in prod:
        if prod[nom] > 100:
            print(nom)
        else:
            print("No hay productos precio superior a 100")
#--- MAIN ---
prod=cargar()
imprimir(prod)
imp_mayor1000(prod)