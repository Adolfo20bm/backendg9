from flask import Flask, request
#es toda la informacion que puedo leer del usuario, dentro de el body
from datetime import datetime

usuarios = [
    {
        'correo': 'ederiveroman@gmail.com',
        'nombre': 'eduardo',
        'apellido': 'de Rivero'
    }
]

# __name__ > muestra si el archivo es el archivo principal del proyecto, mostrara el valor de '__main__' y si no entonces mostrara otro valor
# __name__
#print(__name__)
app = Flask(__name__)

#usaremos el metodo route
#Endpoint es cuando definimos una ruta para que pueda ser accedida
#si no se define que metodo http puede acceder entonce l valor por defecto sera GET

@app.route('/', methods = ['GET'])
def inicio():
    #Controlador (Controller) - la funcionabilidad que tendra mi endpoint
    print('ingreso al endpoint inicial')
    #siempre en todo controlador hay que retornar algo
    return 'Bienvenido a mi primera API en Flask semana 2'

@app.route('/estado', methods=['GET'])
def estado():
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    hora_servidor = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
    return {
        'estado': True,
        'hora': hora_servidor
    }

@app.route('/registrarse', methods=['POST'])
def registro():
    #request.data devuelve el body en binary(formato bytes)
    print(request.data)
    # request.get_json() - convierte la informacion entrante en un dicionario para que pueda ser utilizada sin problemas en python
    print(request.get_json())
    body = request.get_json()
    # iterar el arreglo de usuarios y validar que no existe un usuariocon ese  correo provenieitnte del body
    for usuario in usuarios:
        print(usuario)
        correo = usuario.get('correo')
        if correo == body.get('correo'):
            return{
                'message': 'El usuario ya esta registrado'
            }
    
    #como extraer la informacion de un diccionario
    #body.get('correo')
    #body['correo']
    
    usuarios.append(body)
    # si no existe entonces agregar ese correo al arreglo caso contrario retornar un mensaje que diga que el uusaio ya esta regiostrado
    return {
        'message': 'Usuario registrado exitosamente'
    }

#crear un endpoint que sea /listar-usuarios y este devolbvera el siguiente resultado
# { message: 'Los usuarios son', content: [{},{}]}
@app.route('/listar-usuarios', methods=['GET'])
def listar():
    return {
        'message':'Los usuarios son',
        'content':usuarios

    }


#run sirve para correr nuestro servidor en modo de desarrollo
#si declaramos algo despues del metodo run este nunca se llamara
# por que aca se queda pegado esperado peticiones del cleinte
#debug indicara si guardamos algun archivo dentro
# del proyecto reiniciara automaticamente el servidor
app.run(debug=True)

