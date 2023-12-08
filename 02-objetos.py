class Catalogo:
    socios = []

    def agregar_socio(self,dni, apellido, nombre, edad, plan):
    
        if self.consultar_socio(dni):
          return False
    
        nuevo_socio = {
            'dni': dni,
            'apellido': apellido,
            'nombre': nombre,
            'edad': edad,
            'plan': plan
        }
        self.socios.append(nuevo_socio)
        return True

    def consultar_socio(self,dni):
        for socio in self.socios:
           if socio ['dni']==dni:
              return socio
        return False

    def listar_socios(self):
        print()
        print("_"*50)
        for socio in self.socios:
            print(f'DNI.....: {socio['dni']}')
            print(f'Apellido.....:{socio['apellido']}')
            print(f'Nombre......:{socio['nombre']}')
            print(f'Edad......:{socio['edad']}') 
            print(f'Plan......:{socio['plan']}')
            print("_"*50)

    def modificar_socios(self,dni, nuevo_apellido, nuevo_nombre, nueva_edad, nuevo_plan):
        for socio in self.socios:
           if socio['dni'] == dni:
            socio['apellido'] = nuevo_apellido
            socio['nombre'] = nuevo_nombre
            socio['edad'] = nueva_edad
            socio['plan'] = nuevo_plan
            return True
        return False

    def eliminar_socio(self,dni):
       for socio in self.socios:
          if socio['dni'] == dni:
            self.socios.remove(socio)
          return True
       return False
          

catalogo = Catalogo()
catalogo.agregar_socio(35145879, 'Perez', 'Luciano', 33, 'Full week')
catalogo.agregar_socio(12558691, 'Lopez', 'Carmen', 65, 'Full week')
catalogo.agregar_socio(31556124, 'Arlistan', 'Mariano', 38,
'Starter')

catalogo.listar_socios()

catalogo.modificar_socios(31556124, 'Arlistan', 'Mariano', 39,
'Starter')
catalogo.listar_socios()

catalogo.eliminar_socio(35145879)
catalogo.listar_socios()
'''
    def agregar_socio(dni, apellido, nombre, edad, plan):
    
    if consultar_socio(dni):
        return False
    
    nuevo_socio = {
        'dni': dni,
        'apellido': apellido,
        'nombre': nombre,
        'edad': edad,
        'plan': plan
    }
    socios.append(nuevo_socio)
    return True

def consultar_socio(dni):
    for socio in socios:
        if socio ['dni']==dni:
            return socio
    return False

def listar_socios():
    print()
    print("_"*50)
    for socio in socios:
        print(f'DNI.....: {socio['dni']}')
        print(f'Apellido.....:{socio['apellido']}')
        print(f'Nombre......:{socio['nombre']}')
        print(f'Edad......:{socio['edad']}') 
        print(f'Plan......:{socio['plan']}')
        print("_"*50)

def modificar_socios(dni, nuevo_apellido, nuevo_nombre, nueva_edad, nuevo_plan):
    for socio in socios:
        if socio['dni'] == dni:
            socio['apellido'] = nuevo_apellido
            socio['nombre'] = nuevo_nombre
            socio['edad'] = nueva_edad
            socio['plan'] = nuevo_plan
            return True
    return False

def eliminar_socio(dni):
    for socio in socios:
        if socio['dni'] == dni:
          socios.remove(socio)
          return True
    return False
          
socios = []
agregar_socio(35145879, 'Perez', 'Luciano', 33, 'Full week')
agregar_socio(12558691, 'Lopez', 'Carmen', 65, 'Full week')
agregar_socio(31556124, 'Arlistan', 'Mariano', 38,
'Starter')
agregar_socio(41665891, 'Silvester', 'Carlos', 21,
'Gold')
agregar_socio(35136704, 'Bernardini', 'Camila', 46, 'Starter')
agregar_socio(36589145, 'Rodriguez', 'Luka', 31, 'Full week')

listar_socios()

#modificar_socios(36589145, 'Rodriguez', 'Luka', 32, 'Gold')
eliminar_socio(35136704)

listar_socios()
#print(socios)
#dni_socio = int(input ("Ingrese el dni: "))
#socio = consultar_socio(dni_socio)
#print(f'Resultado: {socio}')
#if socio:
#    print(f'Socio encontrado: {socio['dni']} - {socio['apellido']}')
#else:
#    print(f'Socio {dni_socio} no encontrado')
'''