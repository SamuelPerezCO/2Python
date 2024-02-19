#Profundizando en el tipo str

#Caracteres Bytes
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[0])
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

#Convertit str a bytes
string = 'Programación con Python'
print('String Original:' , string)

bytes = string.encode('UTF-8')
print('bytes codificado:' , bytes)

#Convertir bytes a str
string2 = bytes.decode('UTF-8')
print('String decodificado:' , string2)
print(string == string2)