#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' 
Ejercicio de python 1. 
jose carlos aguayo ortiz
programacion visual
'''











magos = ['mago frank', 'David C', 'Dr. Strange', ' Voldemort']
for valor in magos:
	print(valor)

for valor in range (1,11):
	print (valor)


numeros = list(range(1,11))	
print (numeros)

''' 
Ejercicio de python 2. cuadrado de un numero
jose carlos aguayo ortiz
programacion visual
'''

Cuadrados = []

for num in range(1,11):
    Cuadrados.append(num**2)

print(Cuadrados)

cuadrados2 = [num**2 for num in range(1, 11)]
print('otra forma')

print(min(cuadrados2))
print(max(cuadrados2))
print(sum(cuadrados2))

''' 
Ejercicio de python 3. un millon
jose carlos aguayo ortiz
programacion visual
'''

'''

numeros3 = list(range(1, 1000001))
print (numeros3)

print(min(numeros3))
print(max(numeros3))
'''

cars= ['audi','bmw','subaru','toyota']

for car in cars:
	#print(car)
	if car =='bmw':
		print(car.upper())
	else:
		print(car.title())


respuesta = 17

if respuesta != 42:
	print("esta respuesta no es correcta")


'''
usuarios_baneados = ["pepe charly","jose","maria"]

name = input ("ingresa un nombre de ususario: ")

if name not in usuarios_baneados:
     print(name.title() + "no esta baneado.")

else:
     print(name.title() + "si esta baneado.")     		

edad =  int(input('ingresa tu edad para poder votar'))


print(type(edad))

if edad >= 18:
	print('puedes votar')
else:
	print('no puedes votar perro')	
'''

"""
if - elif- else
la entrada para menores de 4 años es gratiuta
la entrada para cualquier persona entre las edades de 4 y 18 años es de $50
ñaentrada para cualquier persona mayor de 18 es de $100

"""
'''
age = int(input('favor de ingresar tu edad'))
print(type(age))

if age < 4:
	print("tu entrada no tiene costo :)")

elif age <= 18:
	print("tu entrada es de $50")

else:
	print("tu entrada es de $100")
'''
'''
if edad <4:
	precio=0
elif edad <18:
	precio =50
else:
	precio = 100

print("la entrada te va a costar$" + str(precio))
'''

print("programa de operaciones aritmeticas teclee una operacion y dos numeros")

operacion= input("teclee la operacion ")
num1= int(input("teclee el primer numero "))
num2= int(input("teclee el segundo numero "))

if operacion == "suma":
   resultado = num1 + num2
elif operacion == "resta":
	rsultado = num1 - num2
elif operacion == "division":
	oprecion = num1 / num2
else:
	resultado = num1 * num2

print("el resultado de la operacion" + str(operacion) + " es" + str(resultado))


participantes = {
	"nombre":"Edder",
	'edad':37,
	'cursos':['python','react','DJango'],
}

print(participantes['nombre'])
print(participantes['edad'])
print(participantes['cursos'])

participantes['telefono']=9811234567
participantes['ocupacion']= 'Developer'
print("=================")
print(participantes)