#Entrada de datos por consola:
#La entrada de datos se realiza usando la funcion Input() esta funcion pausa la ejecucion del programa
#y espera a que el usuario introduzca algun texto desde el teclado una vez que el usuario presiona enter, el texto
# introducido se devuelve como una cadena (str)

nombre = input('Introduce tu nombre:')
print(f'Recibimos el valor de niombre: {nombre}')

#Pedir edad al usuario ( entra como cadena y lo convertimos a numero)

edad = int(input('Introduce tu edad: '))
print(f'tu edad es: {edad}, y en un año tendras {edad + 1}')
