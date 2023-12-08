import mysql.connector,random

class Catalogo:
    def __init__(self, host, user, password, database):

        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS socios (
            dni INT,
            apellido VARCHAR(255) NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            edad INT(3) NOT NULL,
            plan VARCHAR(255) NOT NULL)''')
        self.conn.commit()

    def agregar_socio(self,dni, apellido, nombre, edad, plan):

        self.cursor.execute(f"SELECT * FROM socios WHERE dni ={dni}")
        socio_existe = self.cursor.fetchone()
        if socio_existe:
            return False
        
        sql = f"INSERT INTO socios (dni, apellido, nombre, edad, plan) VALUES ({dni}, '{apellido}','{nombre}', {edad}, '{plan}')"
        self.cursor.execute(sql)
        self.conn.commit()
        return True
    
    def consultar_socio(self, dni):
        # Consultamos un socio a partir de su dni
        self.cursor.execute(f"SELECT * FROM socios WHERE dni ={dni}")
        return self.cursor.fetchone()
    
    def modificar_socio(self,dni, nuevo_apellido, nuevo_nombre, nueva_edad, nuevo_plan):
        sql = f"UPDATE socios SET apellido = '{nuevo_apellido}', nombre = '{nuevo_nombre}', edad = {nueva_edad}, plan = '{nuevo_plan}' WHERE dni = {dni}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def mostrar_socio(self, dni):
        # Mostramos los datos de un socios a partir de su código
        socio = self.consultar_socio(dni)
        if socio:
            print("-" * 40)
            print(f"dni.....: {socio['dni']}")
            print(f"Apellido: {socio['apellido']}")
            print(f"Nombre...: {socio['nombre']}")
            print(f"Edad.....: {socio['edad']}")
            print(f"Plan.....: {socio['plan']}")
            print("-" * 40)
        else:
            print("Socio no encontrado.")

    def listar_socios(self):
        # Mostramos en pantalla un listado de todos los socios de la tabla
        self.cursor.execute("SELECT * FROM socios")
        socios = self.cursor.fetchall()
        print("-" * 40)
        for socio in socios:
            print(f"dni.....: {socio['dni']}")
            print(f"Apellido: {socio['apellido']}")
            print(f"Nombre...: {socio['nombre']}")
            print(f"Edad.....: {socio['edad']}")
            print(f"Plan.....: {socio['plan']}")
            print("-" * 40)

    def eliminar_socio(self, dni):
        # Eliminamos un socio de la tabla a partir de su dni
        self.cursor.execute(f"""DELETE FROM socios WHERE dni =
        {dni}""")
        self.conn.commit()
        return self.cursor.rowcount > 0

#----------------------------------------------------------------------------------------
# Programa principal


catalogo = Catalogo(host='localhost', user='root', password='',database='miapp')


# Agregamos socios a la tabla


# Socios con plan simple

catalogo.agregar_socio(38259630, 'Lopez', 'Sabrina', 24, 'Simple')
catalogo.agregar_socio(38259631, 'Martinez', 'Juan', 30, 'Simple')
catalogo.agregar_socio(38259632, 'Gomez', 'Mariana', 28, 'Simple')
catalogo.agregar_socio(38259633, 'Rodriguez', 'Jose', 32, 'Simple')
catalogo.agregar_socio(38259634, 'Fernandez', 'Laura', 26, 'Simple')

# Socios con plan premium

catalogo.agregar_socio(38259635, 'Alvarez', 'Pedro', 40, 'Premium')
catalogo.agregar_socio(38259636, 'Sanchez', 'Ana', 35, 'Premium')
catalogo.agregar_socio(38259637, 'Torres', 'David', 37, 'Premium')
catalogo.agregar_socio(38259638, 'Perez', 'Elena', 39, 'Premium')
catalogo.agregar_socio(38259639, 'Gonzalez', 'Cristian', 42, 'Premium')

# Socios con datos aleatorios

for i in range(10):
    catalogo.agregar_socio(random.randint(38250000, 38299999),
                          random.choice(['Lopez', 'Martinez', 'Gomez', 'Rodriguez', 'Fernandez']),
                          random.choice(['Juan', 'Mariana', 'Jose', 'Laura', 'Pedro', 'Ana', 'David', 'Elena', 'Cristian']),
                          random.randint(18, 50),
                          random.choice(['Simple', 'Premium']))




#----------------------------------------------------------------------------------------


# Pruebas realizadas en clase


# Consultamos un socio y lo mostramos
num_dni = int(input("Ingrese el número de DNI: "))
socio = catalogo.consultar_socio(num_dni)
if socio:
    print(f"""Socio encontrado: {socio['dni']} -
    {socio['nombre']}""")
else:
    print(f'Socio {num_dni} no encontrado.')


# Modificamos un socio y lo mostramos
catalogo.mostrar_socio(40352182)
catalogo.modificar_socio(40352182, 'Gomez Jesuita', 'Lucrecio', 30,'Premium')
catalogo.mostrar_socio(40352182)

# Listamos todos los socios
catalogo.listar_socios()

# Eliminamos un socio
catalogo.eliminar_socio(40352182)
catalogo.listar_socios()
