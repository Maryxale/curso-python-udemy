from random import randint

print('***Sistema Generador de ID unico***')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
ano_nacimiento = input('Cual es tu año de nacimiento (YYYY)? ')

#Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
ano_nacimiento_2 =ano_nacimiento.strip()[2:] #para que me de hasta el final

#Valor random
numero = randint(4000, 4050)


#Generamos el valor de id unico (concatenamos)
id_unico = f'{nombre_2}{apellido_2}{ano_nacimiento_2}{numero}'

print(f'''\nHola {nombre},
    Tu nuevo numero de identificacion ID generado por el sistema es: {id_unico}
    Felicidades!
''')

