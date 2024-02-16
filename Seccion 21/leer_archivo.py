archivo = open('C:\\Programacion\\Proyectos\\2Python\\Seccion 21\\prueba.txt' , 'r' , encoding='utf8')
#print(archivo.read())

#Leer algunos caracteres
#print(archivo.read(5))
#print(archivo.read(3))

#Leer lineas completas
#print(archivo.readline())

#Iterar el archivo
#for linea in archivo:
#    print(linea)
#Leer lineas
#print(archivo.readlines())

#acceder a una linea de la lista
#print(archivo.readlines()[0])

#abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('C:\\Programacion\\Proyectos\\2Python\\Seccion 21\\copia.txt' , 'a' , encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se ha terminado el proceso de leer y copiar archivos')
