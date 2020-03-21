def _perimetro(lado):
    p=lado*4
    print("El perímetro es ",p)
def _superficie(lado):
    s=lado*lado
    print("La superficie es ",s)
def dato():
    l=int(input("intro lado del cuadrado: "))
    r=(input("intro para determinar <perImetro> o <superficie> "))

    if r=="perImetro":
        _perimetro(l)
    if r=="superficie":
        _superficie(l)

#programa principal

dato()
