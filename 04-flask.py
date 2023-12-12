#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify
from flask import request
# Instalar con pip install flask-cors
#from flask_cors import CORS
from flask_cors import CORS, cross_origin
# Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
# No es necesario instalar, es parte del sistema standard de Python
import os
import time

app = Flask(__name__)
CORS(app, resources={r"/socios/*": {"origins": "*"}}) #posible correcion para problemas de delete
CORS(app) # Esto habilitará CORS para todas las rutas

class Catalogo:
    # Constructor de la clase
    def __init__(self, host, user, password, database):
       # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password 
    )
        self.cursor = self.conn.cursor()
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
        # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
            # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS socios (
            dni INT,
            apellido VARCHAR(255) NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            edad INT(3) NOT NULL,
            plan VARCHAR(255) NOT NULL)''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

#----------------------------------------------------------------------------

    def listar_socios(self):
        self.cursor.execute("SELECT * FROM socios")
        socios = self.cursor.fetchall()
        return socios

#---------------------------------------------------------------------------
    # def consultar_socio(self, dni):
    #     #Consultamos un socio a partir de su dni
    #     self.cursor.execute("SELECT * FROM socios WHERE dni = {dni}")
    #     return self.cursor.fetchone()

    def consultar_socio(self, dni):
        # Consultamos un socio a partir de su dni
        self.cursor.execute(f"SELECT * FROM socios WHERE dni = {dni}")
        return self.cursor.fetchone()

#--------------------------------------------------------------------------
    def mostrar_socio(self, dni):
    # Mostramos los datos del socio a partir de su dni
        socio = self.consultar_socio(dni)
        if socio:
            print("-" * 40)
            print(f"dni.....:    {socio['dni']}")
            print(f"Apellido: {socio['apellido']}")
            print(f"Nombre...: {socio['nombre ']}")
            print(f"Edad.....: {socio['edad']}")
            print(f"Plan.....: {socio['plan']}")
            print("-" * 40)
        else:
            print("socio no encontrado.")
            
    def agregar_socio(self, dni, apellido, nombre, edad, plan):
    # Verificamos si ya existe un socio con el mismo dni
        self.cursor.execute(f"SELECT * FROM socios WHERE dni = {dni}")
        socio_existe = self.cursor.fetchone()
        if socio_existe:
            return False
    
    # Si no existe, agregamos el nuevo socio a la tabla
        sql = "INSERT INTO socios (dni, apellido, nombre, edad, plan) VALUES (%s, %s, %s, %s, %s)"
        valores = (dni, apellido, nombre, edad, plan)
        self.cursor.execute(sql, valores)   
        self.conn.commit()
        return True
    
    def eliminar_socio(self, dni):
    # Eliminamos un socio de la tabla a partir de su dni    
        self.cursor.execute(f"DELETE FROM socios WHERE dni = {dni}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    def modificar_socio(self, dni, nuevo_apellido, nuevo_nombre, nueva_edad, nuevo_plan):
        sql = "UPDATE socios SET apellido = %s, nombre = %s, edad = %s, plan = %s WHERE dni = %s"
        valores = (nuevo_apellido, nuevo_nombre, int(nueva_edad), nuevo_plan, dni)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
#--------------------------------------------------------------------

# Cuerpo del programa
#----------------------------------------

# Crear una instancia de la clase Catalogo

#catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')
catalogo = Catalogo(host='codoacodogrupo3.mysql.pythonanywhere-services.com', user='codoacodogrupo3', password='mibasededatos', database='codoacodogrupo3$miapp')


@app.route("/socios", methods=["GET"])
def listar_socios():
    socios = catalogo.listar_socios()
    return jsonify(socios)

#-------------------------------------------------------------------
@app.route("/socios/<int:dni>", methods=["GET"])
def mostrar_socio(dni):
    socio = catalogo.consultar_socio(dni)
    if socio:
        return jsonify(socio)
    else:
        return "Socio no encontrado", 404 
     
@app.route("/socios", methods=["POST"])
def agregar_socio():
    # Recojo los datos del form
    dni = request.form['dni']
    apellido = request.form['apellido']
    nombre = request.form['nombre']
    edad = request.form['edad']
    plan = request.form['plan']
    if catalogo.agregar_socio(dni, apellido, nombre, edad, plan):
        return jsonify({"mensaje": "Producto agregado"}), 201
    else:
        return jsonify({"mensaje": "Producto ya existe"}), 400
    
# @app.route("/socios/<int:dni>", methods=["DELETE"])
# def eliminar_socio(dni):
#     socio = catalogo.consultar_socio(dni)
#     if socio:
#     # Luego, elimina el socio del catálogo
#         if catalogo.eliminar_socio(dni):
#             return jsonify({"mensaje": "socio eliminado"}), 200
#         else:
#             return jsonify({"mensaje": "Error al eliminar el socio"}),500
#     else:
#         return jsonify({"mensaje": "socio no encontrado"}), 404

@app.route("/socios/<int:dni>", methods=["OPTIONS", "DELETE"])
def eliminar_socio(dni):
    if request.method == "OPTIONS":
        # Manejar la solicitud OPTIONS aquí
        response = app.make_default_options_response()
    elif request.method == "DELETE":
        socio = catalogo.consultar_socio(dni)
        if socio:
            # Luego, elimina el socio del catálogo
            if catalogo.eliminar_socio(dni):
                response = jsonify({"mensaje": "socio eliminado"}), 200
            else:
                response = jsonify({"mensaje": "Error al eliminar el socio"}), 500
        else:
            response = jsonify({"mensaje": "socio no encontrado"}), 404
    else:
        # Manejar otros métodos si es necesario
        response = jsonify({"mensaje": "Método no permitido"}), 405

    # Configurar encabezados CORS
    response.headers['Access-Control-Allow-Origin'] = '*'  # O restringir a tus dominios permitidos
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    return response

@app.route("/socios/<int:dni>", methods=["PUT"])
@cross_origin()
def modificar_socio(dni):
# Recojo los datos del form
    nuevo_apellido = request.form.get("apellido")
    nuevo_nombre = request.form.get("nombre")
    nueva_edad  = request.form.get("edad")
    nuevo_plan = request.form.get("plan")
    # Actualización del socio
    if catalogo.modificar_socio(dni, nuevo_apellido, nuevo_nombre, nueva_edad, nuevo_plan):
        return jsonify({"mensaje": "socio modificado"}), 200
    
if __name__ == "__main__":
    app.run(debug=True)    


@app.route("/")
def index():
    return "¡La aplicación Flask está en funcionamiento!"
