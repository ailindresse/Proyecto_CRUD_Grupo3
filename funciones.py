def agregar_socio(dni, apellido, nombre, edad, plan):

 if consultar_socio(dni):
   return False
nuevo_producto = {
  'dni': dni,
  'apellido': apellido,
  'nombre': nombre,
  'edad': edad,
  'plan': plan
}
socios.append(nuevo_socio)
return True

socios = []
agregar_socio(35145879, 'Perez', Luciano, 33, 'Full week')
agregar_socio(12558691, 'Lopez', Carmen, 65, 'Full week')
agregar_socio(31556124, 'Arlistan', Mariano, 38,
'Starter')
agregar_socio(41665891, 'Silvester', Carlos, 21,
'Gold')
agregar_socio(26335189, 'Bernardini', Camila, 46, 'Starter')
agregar_socio(36589145, 'Rodriguez', Luka, 31, 'Full week')

print(socios)
