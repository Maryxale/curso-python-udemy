#Conversion de tipos de datos

#Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numerico en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')
#de igual forma se cambia cuando es de caden a float y cuando es de numero a cadena str

#covertir a booleano
#Tipo bool es Falso en los siguientes casos:
#Si el valor es 0, cadena vacia, o None, entonces regresa False
#Regresa True, en caso contrario

numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de 0: {booleano}') #False

numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de 5: {booleano}') #True

cadena = ''
booleano = bool(cadena)
print(f'Valor booleano de una cadena vacia: {booleano}') #cadena vacia es igual a 0 
