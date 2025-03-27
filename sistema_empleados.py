print('***Sistema de Empleados***')
nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input('Es jefe de departamento (Si/No)?')

#Vamos a convertir a un tipo bool la variable es_jefe_departamento
#se tiene que agragar una logica extra para solicitar datos de tipo booleano
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

#Imprimir lo valores del empleado
print('\nDatos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}') #el punto para indicar los decimales que se quieren imprimir, 2 la cantidad y f que es flotante
print(f'es jefe de departamento? {es_jefe_departamento}')