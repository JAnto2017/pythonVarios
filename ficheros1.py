"""
para abrir archivo 'identificador=open(nombre_archivo,modo)
modo: variable que indica acciones sobre el archivo
   'r' abrir para lectura
   'w' abrir para escritura si existe, borra
   'a' abrir para escritura si existe, añade 
   'r+'abrir para lectura y escritura
identificador: variable referencia al archivo
"""
#programa MAIN
iden = open('perros.txt','w')   #crea archivo nuevo para escritura
iden.write("collie \n")
iden.write("cocker \n")
iden.write("poodle \n")         #en la escritura poner \n
iden.close()