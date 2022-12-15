alumnos = [
  {
    "id": 1,
    "nombre": "Eduardo",
    "dni": 76543210,
    "status": True
  },
  {
    "id": 2,
    "nombre": "Jorge",
    "dni": 76543354,
    "status": True
  },
  {
    "id": 3,
    "nombre": "Raul",
    "dni": 76543233,
    "status": True
  },
  {
    "id": 4,
    "nombre": "Miguel",
    "dni": 24543210,
    "status": False
  },
  {
    "id": 5,
    "nombre": "Jose",
    "dni": 76663210,
    "status": False
  }
]

#extraer nombre soilo si el alumno eta activo
def extraerNombre(lista_alumnos):
    for alumno in lista_alumnos:
        if alumno['status'] == True:
            print(alumno['nombre'])
        else:
            pass
    #print()

#extraerNombre(alumnos)    

alumnos_activos = []

def obtenerAlumnosActivos(lista_alumnos):
    for alumno in lista_alumnos:
        if alumno['status'] == True:
            alumnos_activos.append(alumno)

#obtenerAlumnosActivos(alumnos)
#print(alumnos_activos)

#Funcion que cuente la cantiodad de palabras que contenga una frase

#frase=[]
#ingresofrase = input('Ingrese su frase ')
#frase.append(ingresofrase)
#print()



def contarPalabras():
    frase= input('Ingrese su frase: ')
    espacios = 1
    for letra in frase:
        if letra == ' ':
            espacios = espacios + 1
    return espacios      

print(contarPalabras())