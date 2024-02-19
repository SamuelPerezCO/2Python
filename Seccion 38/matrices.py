#Matrices
matriz = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(f'Matriz original: {matriz}')
print(f'Renglon 0, Columna 0: {matriz[0][0]}')
print(f'Renglon 2, Columna 2: {matriz[2][2]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

lista_listas = [[10 , 14 , 87, 90 , 71] , [4 , 5 , 6 , 7 ] , [9 , 0 , 11 , 15 , 45 , 61 , 70]]
lista_listas.sort(key=len)
print(f'Ordenar lista:{lista_listas}')

#sorted built - in

#help(sorted)
nombres1 = ['Juan Carlos' , 'Karla' , 'Pedro' , 'Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)

#Ordenar de manera descendente
nombres1 = sorted(nombres1 , reverse = True)
print(nombres1)

#Ordenar por la cantidad de caracteres (largo)
nombres1 = sorted(nombres1 , key = len)
print(nombres1)

#built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))