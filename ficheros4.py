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
#para convertir datos numericos a alfanumericos usar 'str()'
#usamos \t espacio de tabulador
#usamos %s para indicar string y usamos %a para indicar dato numerico

#MAIN
a=3.2316
archivo = open("jugador2.txt","w")
datos = ["Pérez \t 12 \n","Mario \t 13 \n",'%s' %a]
archivo.writelines(datos)
archivo.close()