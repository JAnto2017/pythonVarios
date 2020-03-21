#PRIMERA FUNCION SUMA TODOS LOS ELEMENTOS DE LA LISTA
def suma(lista):
    s=0
    for x in range(len(lista)):
       s+=lista[x] 
    return s

#SEGUNDA FUNCION DEVUELVE EL NUMERO MAYOR
def mayor(lista):
    m=lista[0]
    for x in range(1,len(lista)):
        if m<lista[x]:
            m=lista[x]
    return m

#TERCERA LISTA DEVUELVE EL NUMERO MENOR
def menor(lista):
    r=lista[0]
    for x in range(1,len(lista)):
        if r>lista[x]:
            r=lista[x]
    return r

#MAIN
lista=[10,56,23,120,94]
print('Lista completa: ',lista)
print('La suma de elementos lista: ',suma(lista))
print('El mayor elemento es:       ',mayor(lista))
print('El menor elemento es:       ',menor(lista))