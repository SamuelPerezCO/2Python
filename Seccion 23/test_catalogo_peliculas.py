from dominio.Pelicula import *
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None

opciones = """
Opciones:
1. Agregar Pelicula
2. Listar Peliculas 
3. Eliminar Catalogo Peliculas
4. Salir
"""
while opcion != 4:
    try:
        print(opciones)
        opcion = int(input('Escribe tu opcion (1 - 4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del programa')