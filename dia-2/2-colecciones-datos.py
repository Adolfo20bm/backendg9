#Tuplas
#son ordenadas PERO no se pueden modificar(una vez definidas no se pueden alterar)

cursos = ('backend','frontend')
mix=(1,80.2, False, 'Eduardo', (1,2,3))
#para entrara a las posiciones es con los corchetes
print(cursos[0])

print(cursos[:1])

# ni agregar
# cursos.append('design')

# ni editar
#cursos[0] = 'mobile'

# ni eliminar
#del cursos[0]

print(cursos)
print(len(cursos))

#Para mayor info docs.python.org

#Conjunto (Set)
#Coleccion de datos desordenada una vez creada ya no se puede acceder mediante sus posiciones pero si se puede modificar

primos = {1,3,5,7,11,17,19}
estaciones = {'verano','otoño','primavera','invierno'}

print(primos)
print(estaciones)
print(17 in primos)
#  se pude agregar nuevos elementos a un set
print.add(23)
print(primos)

#se puede eliminar
primos.pop()
print(primos)

#----------------------------
# Diccionarios
#coleccion ordenada pero por llaves(no po indices) y editabe

persona = {
    'nombre': 'eduardo',
    'apellido': 'suarez',
    'correo': 'eduardo@gmail.com',
    'telefono': '+459565235'
}

print(persona['nombre'])
print(persona['direccion'])

#get retorna el valor de la llave si la llave esta en el diccionarios ino el valor por fdefecto m el varlo rpor defecto es vacion
print(persona.get('direccion','No hay'))

#como saber todas las llaves de ese diccionario
print(persona.keys())

#eso devuelve todos los valores
print(persona.values())

#agregamos
persona['nombre'] ='Lisbeth'
persona['direccion'] = 'calle los dragones'
print(persona)

#remueve el valor de esa llave y la elimina y opcionalmente podemos almacenar el valor en otra variable
correo_eliminado = persona.pop('correo')
print(persona)
print(correo_eliminado)









