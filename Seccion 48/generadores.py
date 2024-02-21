# Generadores
# Es una funcion especial , retorna una secuencia de valores
# SUspende la ejecucion de la funcion yield ( producir)  (no se usa return)

def generador():
    yield 1
    print('Se reanuda la ejecuccion')
    yield 2
    print('Se reanuda la ejecuccion')
    yield 3

#consumir el generador a demanda
gen = generador()
#COn cada llamada consumimos un valor 
print(next(gen))
print(next(gen))
print(next(gen))
#Si tratamos de consumir mas valores de los que produce el generador
#Lanza errores de stopiteration

#Consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Numero: {valor}')