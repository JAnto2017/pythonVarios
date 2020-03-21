#ejercicio58 Tipos de datos

print("Datos primera persona")
nombre1=input("Ingrese nombre: ")
edad1=int(input("Ingrese la edad: "))
altura1=float(input("Ingrese atura: "))

print("Datos segunda persona")
nombre2=input("Nombre? ")
edad2=int(input("Edad? "))
altura2=float(input("Altura "))

print("Más alta es: ")
if altura1>altura2:
    print(nombre1)
else:
    print(nombre2)
