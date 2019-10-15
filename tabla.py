numero=int(input("ingrese el numero para mostrar su tabla"))
rango=range(1,11)
for elemento in rango:
	producto = numero*elemento
	print(numero,"x",elemento,"x",producto)