def miFuncion():
    print('Hola Mundo')

def suma(a,b):
    return a+b

def comprobarEdad(edad):
    if(edad>=18):
        return 'eres mayor de edad'
    else:
        return 'No eres mayor de edad, no puedes ingresar'

edad = input('Ingrese su edad: ')
edad = int(edad)

#miFuncion()
#print(suma(3,5))
#print(comprobarEdad(10))
#par aver el tipo de variable    --->   print(type(edad))
#print(comprobarEdad(edad))

alumnos = ['eduardo','Pepe','Jose','Miguel','Julia','Raul']

def buscarNombre():
    if not 'Eduardo' in alumnos:
        return False
    return True

#Ingresar una lista de nombres(4 nomrbres) y que una funcion haga la busqueda del ultimo nombre(5to nombre)

nombres=[]

p_nombre = input('Ingrese el nombre 1')
s_nombre = input('Ingrese el nombre 2')
t_nombre = input('Ingrese el nombre 3')
c_nombre = input('Ingrese el nombre 4')
q_nombre = input('Ingrese el nombre 5')

nombres.append(p_nombre)
nombres.append(s_nombre)
nombres.append(t_nombre)
nombres.append(c_nombre)
nombres.append(q_nombre)

nombre_a_buscar = input('Ingrese el nombre a buscar')

def buscarPersona(nombre):
    if nombre in nombres:
        #el format lo va a insertar en la llave
        return '{} ha sido encontrado {}'.format(nombre, 'textoo')
    return 'No pudimos encontrar a {}'.format(nombre)

print(buscarPersona(nombre_a_buscar))