#Bool contiene los valores de true y false
#Tipo numericos , False para 0 y true para los demas valores
valor = 0
resultado = bool(valor)
print(f'Valor {valor} , resultado {resultado}')

valor = 15
resultado = bool(valor)
print(f'Valor {valor} , resultado {resultado}')

#Tipo str, False para '', True demas valores
valor = ''
resultado = bool(valor)
print(f'Valor {valor} , resultado {resultado}')
valor = 'Hola'
resultado = bool(valor)
print(f'Valor {valor} , resultado {resultado}')

#Tipo Coleccion , false para coleccion vacias , True para todas las demas colecciones
#Lista
valor = []
resultado = bool(valor)
print(f'Valor {valor} , resultado: {resultado}')

valor = [2 , 3 , 4]
resultado = bool(valor)
print(f'Valor {valor} , resultado: {resultado}')

#Tupla
valor = ()
resultado = bool(valor)
print(f'Valor {valor} , resultado: {resultado}')

valor = (2 , 3 , 4)
resultado = bool(valor)
print(f'Valor {valor} , resultado: {resultado}')

#Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor {valor} , resultado: {resultado}')

valor = {'nombre':'Juan' , 'apellido':'Perez'}
resultado = bool(valor)
print(f'Valor {valor} , resultado: {resultado}')

variable = 10
if bool(variable):
    print('Regreso verdadero')
else:
    print('Regreso falso')

if variable:
    print('Regreso Verdadero')
else:
    print('Regreso falso')

while variable:
    print('Ejeccion ciclo while')
    break
else:
    print('fin ciclo while')