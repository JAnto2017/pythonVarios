#uso de continue

lista = [1,2,3,4,5,6]

for element in lista:
    if element == 2:
        continue
    if element == 5:
        break
    print("Elemento = "+str(element))