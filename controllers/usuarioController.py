#flask-restful brinda sooporte para crear una api rest
from flask_restful import Resource, request
from config import conexion

class UsuariosController(Resource):
    #los metodos que nosotros queramos utilizar (GET, POST) lo tendremos que definir como metodo de la clase
    def get(self):
        return {
            'message': 'Yo soy el get del usuario'
        }
    def post(self):
        body = request.get_json()
        print(body)
        return {
            'message': 'Yos soy el post del usuario'
        }