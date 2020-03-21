def titulo(tit,carac="*"):
    print(tit)
    print(carac*len(tit))

#parametros por defecto
def sumar(v1,v2,v3=0,v4=0,v5=0):
    s=v1+v2+v3+v4+v5
    return s

#main
titulo("sistema de administracion")
titulo("ventas","-")
print("La suma 5+6 = ",sumar(5,6))
print("La suma 1+2 = ",sumar(1,2,3))
print("La suma 1+2+3+4+5 = ",sumar(1,2,3,4,5))