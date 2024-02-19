#Profunfizando str

#Caracteres unicode
print('Hola\u0020Mundo')
print('Notacion simple: ','\u0041')
print('Notacion extendida: ' ,'\U00000041')
print('Notaion hexadecimal: ','\x41')
print('Corazon: \u2665')
print('Cara sonriendo: \U0001f600')
print('Serpiente: \U0001f40d')

print('Ascii'.center(50 , '-'))
#Caracteres Ascii
caracter = chr(65)
print(f'A Mayuscula: {caracter}')

caracter = chr(64)
print(f'Simbolo @ : {caracter}')

caracter = chr(97)
print(f'a minuscula: {caracter}')