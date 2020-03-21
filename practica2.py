num1=int(input("Intro primer valor: "))
num2=int(input("Intro otro valor: "))
num3=int(input("rango de valores: "))

if num1<num2 and num1<num3:
    print(num1)
else:
    if num2<num3:
        print(num2)
    else:
        print(num3)

if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
