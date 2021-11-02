#--------------------------------- Listas
lis_1 = list([1,2,3])
lis_2 = [1,'a',list(),dict()]
print ("Lista. ",lis_1)
print ("Lista. ",lis_2)
#--------------------------------- Tuplas (son inmutables)
tup_1 = tuple([1,2,3])
print ("Tupla: ",tup_1)
#--------------------------------- Diccionarios {key:value}
dic = ({'Sevilla':1,'Madrid':2,'Santander':3})
print("Diccionario: ",dic)
print(dic['Sevilla'])
#print(dic[1]) este causa error
print(dic.keys())
print(dic.values())
#--------------------------------- Set {para valores únicos}
set_1 = {1,2,3,4,5}
print("Set con valores únicos: ",set_1)
lista = [1,2,3,4,5,6,7,8,8,4,9]
print("Lista con valores repetidos: ",lista)
set_2 = set(lista)
print("Conversión a set: ",set_2)