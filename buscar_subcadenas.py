#Buscar Subcadenas
#find devuelve el indice de la primera aparicion de la subcadena que se pide
#cuando find no encuentra el indice de la subcadena que se le pide,devolvera -1
cadena = 'Hola, mundo!'
indice = cadena.find('mundo')
print(f'Indice de la subcadena de mundo: {indice}')

#Obtenemos el indice de la subcadena de Hola
indice = cadena.find('Hola')
print(f'Indice de la subcadena de Hola: {indice}')
