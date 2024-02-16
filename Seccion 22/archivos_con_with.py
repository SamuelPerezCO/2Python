from ManejoArchivos import ManejoArchivos

# with open('prueba.txt','r', encoding='utf8') as archivo:
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

#Si intenta ejecutarlo no da por el hecho de la ubicacion del archivo .txt
    