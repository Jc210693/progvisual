nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
person = {'nombre': nombre, 'edad': edad, 'direccion': direccion , 'telefono': telefono}
print(person['nombre'], 'tiene', person['edad'], 'años, vive en', person['direccion'], 'y su número de teléfono es', person['telefono'])