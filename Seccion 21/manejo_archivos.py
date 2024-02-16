try:
    archivo = open('C:\\Programacion\\Proyectos\\2Python\\Seccion 21\\prueba.txt' , 'w' , encoding='utf8')
    archivo.write('Agregamos información al archivo \n ')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('fin del archivo')