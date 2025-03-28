#Crear un email
#Nota: con control R se reemplaza una variable por otro nombre

nombre_usuario = ' Ubaldo Acosta Soto '
print(f'Nombre de usuario: {nombre_usuario}')
#Normalizamos el nombre del Usuario
nombre_usuarioNormalizado = nombre_usuario.strip()
#Reemplazar espacios por puntos
nombre_usuarioNormalizado = nombre_usuarioNormalizado.replace(' ','.')
#covertir a minusculas
nombre_usuarioNormalizado = nombre_usuarioNormalizado.lower()
print(f'Nombre del usuario Normalizado: {nombre_usuarioNormalizado}')

#Datos de la empresa

nombre_empresa = ' Global Mentoring '
print(f'nombre de la empresa: {nombre_empresa}')
extension_dominio = '.com.mx'
print(f'extension del dominio: {extension_dominio}')

#Quitamos espacios en blanco y convertimos a minisculas
nombre_empresa_normalizada = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizada}{extension_dominio}'
print(f'Dominio del email normalizado: {dominio_email_normalizado}')
#Creamos el email final

email = f'{nombre_usuarioNormalizado}{dominio_email_normalizado}'
print(f'\nEmail finalizado: {email}')


