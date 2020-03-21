#Tabla de multiplicar del parAmetro enviado
def tabla(num,term=10):
    for x in range(term):
        va = x * num
        print(va,",",sep="",end="")
    print()

#main
print("Tabla del ... 3")
tabla(3)
print("Tabla del ... 3 con 5 tErminos")
tabla(3,5)
print("Tabla del ... 3 con 20 tErminos")
tabla(term=20,num=3)