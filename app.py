from flask import Flask
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api

from config import conexion
from models.usuarios import UsuarioModel
from models.tareas import TareaModel
from controllers.usuarioController import UsuariosController


load_dotenv()

app = Flask(__name__)

#inicializamos la clase api qe nos sevira para poder utilizar todos los controles dentro de la aplicaion de flask
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

#ingresa a la carpeta dia-1 y corre el app.py par levantar e lservidor
#cd dia-1
#py app.py

#crea la carpeta models dentro del proyecto

#saca el pip freeze de otro proyecto e instalalo en tu proyeto, sca el requirements tambien

#hasta aqui
#git add -A 
#git commit -m "requirements.txt"
# git commit -m "librerias para el proyecto"

#------>>>>>>>

#Ahora continuamos en usuarios

#REGRESAMOS A app.py

#inicializamoas la isntancoa de flask alchemisr con las propiedades seteadas en la aplicacion Flask
conexion.init_app(app)
#Inicializamos la clase Migrate con la configuracion de nuestra base de datos y aplicacion de flask
migrate = Migrate(app, conexion)

#declarar todas las rutas que vamos a utilizar mediante lo scontroladores
api.add_resource(UsuariosController, '/usuarios')

#git log para ver los cambios que se ahan hecho en prouecto

#en terminal has:  flask db init
#saldra error de URI ALCHEMIST

#Entonces se agrega en app.py
# from os import environ
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

#ahora instala la libreria para .env
#pip install python-dotenv
#importamos

# crea el archivo .env


#ejecutamos el comando en terminal
# flask db init
#se creara una carpeta migrations
# ->versions
# alembic
# -env
# -readme
# -script

if __name__=='__main__':
    app.run(debug=True)