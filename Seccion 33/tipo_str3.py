#Profundizando en el tipo str

#Multiplicacion str
resultado = 5*'Hola'
#print(f'Resultado {resultado}')

#Multiplicaccion tuplas 
resultado = 5*('Hola' , 10)
#print(f'Resultado {resultado}')

#Multiplicacion Listas
resultado = 10 * [0]
#print(f'Resultado {resultado} , largo {len(resultado)}')

#Caracteres de escape
resultado = 'Hola \' Mundo'
print(f'El Resultado: {resultado}')

resultado = 'Se va a eliminar el punto.\b\b\b'
print(f'El Resultado: {resultado}')

#Caracter \
resultado = 'c:\\directorio\\juan'
print(f'El Resultado: {resultado}')

#raw string
resultado = r'Cadena con \n salto de linea'
print(f'El Resultado: {resultado}')