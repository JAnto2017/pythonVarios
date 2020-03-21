apro=0
rep=0
for x in range(10):
    nota=int(input("Ingrese nota: "))
    if nota>=7:
        apro=apro+1
    else:
        rep=rep+1
print("Aprobados ")
print(apro)
print("Reprobados ")
print(rep)
