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
#MAIN
var_num=12
archivo=open("archivo.dat","w")
archivo.write("Pérez \t %s" %var_num)
archivo.close()