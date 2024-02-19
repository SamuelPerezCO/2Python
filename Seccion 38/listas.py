#Profundizando Listas
#Listas son mutables

nombres1 = ['Juan' , 'Karla' , 'Pedro']
nombres2 = 'laura Maria Gonzalo Ernesto'.split()
#Sumar listas
print(f'Sumar Listas {nombres1 + nombres2}')
#Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender la lista1 con la lista2: {nombres1}')

#Lista de numeros
numeros1 = [10 , 40 , 15 , 4 , 20 , 90, 4]
print(f'Lista original: {numeros1}')
#obtener el indice del primero elemento encontrado en una lista
#help(list.index)
print(f'indice 4: {numeros1.index(4)}')

#Invertir el orden de los elementos de una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

#Ordenar los elementos de una lista
numeros1.sort()
print(f'Lista ascendente: {numeros1}')
#Ordenar de manera descendete una lista
numeros1.sort(reverse = True)
print(f'Lista ordena(descendente) {numeros1}')

#Obtener el valor minimo y max de una lista
print(f'Valor minimo: {min(numeros1)}')
print(f'Valor Maximo: {max(numeros1)}')

#Copiar los elementos de una lista 
numeros2 = numeros1.copy()
#help(list.copy)
print(f'Misma Referencia? {numeros1 is numeros2}')
print(f'Mismo Contenido? {numeros1 == numeros2}')

#Podemos usar el constructo de la lista
numeros2 = list(numeros1)
print(f'Misma Referencia? {numeros1 is numeros2}')
print(f'Mismo Contenido? {numeros1 == numeros2}')

#slicing
numeros2 = numeros1[:]
print(f'Misma Referencia? {numeros1 is numeros2}')
print(f'Mismo Contenido? {numeros1 == numeros2}')

#Multiplicacion Listas
lista_multiplicacion = 5 * [[2 , 5]]
print(lista_multiplicacion)
print(f'Misma referencia: {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Misma contenido: {lista_multiplicacion[0] == lista_multiplicacion[1]}')
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)
