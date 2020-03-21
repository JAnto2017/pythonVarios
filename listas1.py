#almacena una lista de 5 elementos las tuplas empleados y sueldo
#---------- carga empleados
def cargar():
    empleados=[]
    for x in range(5):
        nombre=input("Nombre empleado: ")
        sueldo=int(input("Sueldo: "))
        empleados.append((nombre,sueldo))
    return empleados
#---------- imprime
def imprimir(empleados):
    print("Listado empleados + sueldos")
    for nombre,sueldo in empleados:
        print(nombre,sueldo)
#---------- nombra empleados con mayor sueldo
def mayor_sueldo(empleados):
    empleado=empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado=emp
    print("Empleado: ",empleado[0],"sueldo: ",empleado[1])
#---------- cantidad de empleados con sueldo < 1000
def sueldos_menor1000(empleados):
    cant=0
    for empleado in empleados:
        if empleado[1]<1000:
            cant+=1
    print("Nº empleados sueldo<1000: ",cant)
#---------- MAIN
empleados=cargar()
imprimir(empleados)
mayor_sueldo(empleados)
sueldos_menor1000(empleados)