#Generador de Emails
print('***Generador de Emails***')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
empresa = input('Ingrese el nombre de la empresa: ')
dominio = input('Ingrese el dominio: ')

#Normalizar los valores
nombre = nombre.strip().lower().replace(' ','.')
apellido = apellido.strip().lower().replace(' ','.')
empresa = empresa.strip().lower().replace(' ','')
dominio = dominio.strip().lower().replace(' ','')

#generar el email
email = f'{nombre}.{apellido}@{empresa}{dominio}'

print(f'''
Tu nuevo email generado por el sistema es:
    {email}
''')