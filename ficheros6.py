"""
https://github.com/JAnto2017/pythonVarios.git
para abrir archivo 'identificador=open(nombre_archivo,modo)
modo: variable que indica acciones sobre el archivo
   'r' abrir para lectura
   'w' abrir para escritura si existe, borra
   'a' abrir para escritura si existe, añade 
   'r+'abrir para lectura y escritura
identificador: variable referencia al archivo
"""
#creaciOn de tablas en un archivo

#MAIN
dat=[[1.2,3.0,-7.45],
     [-8.3,6,17.563],
     [98.78,-12.5,-46.2332],
     [2,-567.2,8.43],
     [1,0,1.2013]]
archivo = open("tabla.dat","w")
for f in dat:
    for c in f:
        archivo.write("%14.8f" %c)
    archivo.write("\n")
archivo.close()