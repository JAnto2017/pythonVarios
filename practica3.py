mul3=0
mul5=0
for x in range(10):
    valor=int(input("input valor: "))
    if valor%3 == 0:
        mul3=mul3+1
    if valor%5 == 0:
        mul5=mul5+1
print("Cantidad multiplos de 3")
print(mul3)
print("Cantidad multiplos de 5")
print(mul5)
