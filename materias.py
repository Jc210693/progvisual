numero = int(input("Dígame cuántas materias tiene: "))

if numero < 1:
    print("¡Teclee por lo menos una!")
else:
    lista = []
    for i in range(numero):
        print("Escriba el nombre de la materia", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("Las materias son:", lista)