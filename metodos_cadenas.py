#Metodos de cadenas

cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}') #formateo de cadena
mayusculas = cadena1.upper() #para convertir a mayusculas
print(f'Cadena en mayusculas: {mayusculas}')
print(f'Cadena en minusculas: {cadena1.lower()}') #asi no se usa una variable diferente sino que por la misma se manda a llamar
#lower para convertir a minusculas

cadena2 = ' Juan Perez '
print(f'Cadena con espacios: {cadena2}')
print(f'Cadena sin espacios: {cadena2.strip()}') #para eliminar espacios al inicio y al final
