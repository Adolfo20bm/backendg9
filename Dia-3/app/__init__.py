from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hola soy un servidor de Flask'
usuarios = [
    {
        "nombre": "Paolo",
        "dni":"77777777"
    },
    {
        "nombre": "Adolfo",
        "dni":"99999999"
    }
]

@app.route("/<dni>")
def home(dni):
    return f'Hola tu numero de DNI es {dni}'
