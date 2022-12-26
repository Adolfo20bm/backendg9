from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from os import environ

#sirve para leer el archivo .env y cargar las variables definidas e ese archivo como varialbes de entorno
from dotenv import load_dotenv

load_dotenv()
#print(environ)

app = Flask(__name__)
#todas las variables de entorno siempre seran string

app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT'))

#print(app.config)
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def inicio():
    return {
        'message': 'Bienvenido a mi API de colegios'
    }

@app.route('/inicio', methods=['GET'])
def pagina_inicio():
    return render_template('inicio.html')

@app.route('/mostrar-alumnos', methods=['GET'])
def devolver_alumnos():
    #crea conexion
    cursor = mysql.connection.cursor()
    #clausuala a determinada tabla
    cursor.execute("SELECT * FROM alumnos")
    #devolver toda la info de esa consulta
    resultado = cursor.fetchall()
    #print(resultado)
    resultado_final = []
    for alumno in resultado:
        alumno_diccionario = {
            'id': alumno[0],
            'nombre': alumno[1],
            'ape_paterno': alumno[2],
            'ape_materno': alumno[3],
            'correo': alumno[4],
            'num_emergencia': alumno[5],
            'curso_id': alumno[6]
        }
        print(alumno_diccionario)
        resultado_final.append(alumno_diccionario)

#    return {
#        'message': 'Los alumnos son:',
#        'content': resultado_final
#    }

    return render_template('mostrar_alumnos.html', alumnos=resultado_final, mensaje='Hola desde Falask')

@app.route('/agregar-alumno', methods=['GET','POST'])
def agregar_alumno():
    print(request.method)
    if request.method == 'GET':
        return render_template('agregar_alumno.html')
    elif request.method == 'POST':
        body = request.get_json()
        #print(body)
        cursor = mysql.connection.cursor()
        # al poner el % luego del string es lo mismo que utilizar el metodo .format
        cursor.execute("INSERT INTO alumnos (id, nombre, ape_paterno, ape_materno, correo, num_emergencia) VALUES (DEFAULT, '%s', '%s', '%s', '%s', '%s' )" % (
            body.get('nombre'), body.get('ape_paterno'), body.get('ape_materno'), body.get('correo'), body.get('num_emergencia')))
        # indicamos a la base de datos que esa insercion tiene que perdurar (de manera permanente)
        mysql.connection.commit()
        # cerrar la conexion con la base de datos
        cursor.close()
        return {
            'message': 'Alumno agregado exitosamente'
        }

app.run(debug=True)



