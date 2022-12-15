#Operadores aritmeticos
numero1, numero2 = 10,10
# a
# b
# c
# d

#SUMA
#Nota: solamente sera suma si las dos variables son numericos, si es que son string entonces se hara una concatenacion y ademas no se puede sumar entre string y numeros

print(numero1+numero2)

#RESTA
print(numero1-numero2)
#MULTIPLICAION
#Nota si se usa la multiplicaion en un string, entonces este repetira el numero de veces un string y un numero de veces

print(numero1*numero2)
print('Hola'*5)
#DIVISION
print(numero1/numero2)

#MODULO
print(numero1%numero2)

#Cociente
print(numero1//numero2)

#exponente
print(numero1**numero2)

print(numero1**0.5)

#----------------------------
#OPERADORES ASIGNACION
#IGUAL asignar un nuevo valor del numero1 en una unidad

numero1 += 1 #incremento el valor del numero1 en una unudad
print(numero1)

#DECREMENTO
numero1 -= 1 #numero1= numero1-1
print(numero1)
#Multiplicador
numero1 *= 2
print(numero1)

#DIVIDENDI
numero1 /=5 #numnero1 = numero1/5
print(numero1)

#-----------------------
#OPERADORES DE COMPARACION Siempre retornaran un booleano(si es verdadero o falso)

#IGUAL QUE
#Nota: en python a diferencia de js no existe el triple igual(comparador de tipo de datop)
print(numero1) #Float
print(40) # Int
print(numero1 == numero2)
print(int(40.999999))
print(type(numero1) == type(numero2))
#en js ===
# 10 === '10'
#false
#valida el contenido y valida tambien el tipo de dato

#MAYOT | MAYOR IGUAL
print(10 > 9.58)
print(10 > int('5'))
print(50 >= 30)

# MENOR | menor o igual
print(50 < 80)
print(10 <= 50)

print(100>= int(float("40.24")))

#-----------------------
#OPERADORES DE LOGICOS
#  and &&
#  || para OR

eduardo=30
ronald=25
henry=25
carmen=19
angel=15

print((angel > eduardo) and (ronald < henry))
print((eduardo > angel) and (carmen < ronald))

print((carmen < ronald) or (eduardo < ronald))

#  OPERADORES DE IDENTRIDAD
verduras = ['A','B','C']

print('A' in verduras)
print('C' not in verduras)






