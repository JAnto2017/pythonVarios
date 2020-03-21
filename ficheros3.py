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
#Uso de instruccion 'with' lectura-escritura cierre automatico
with open("jugador.txt","w") as identif:
    identif.writelines(["Pérez \n","Mario \n"])