peso=  float(input("Escribe tu peso: "))
estatura= float(input("Escribe tu estatura: "))

imc= peso/estatura**2


if imc<15:
   estado = "Delgadez muy severa"
elif imc<=15.9:
    estado = "Delgadez severa"
elif imc <=18.4:
    estado = "Delgadez"
elif imc <=24.9:
    estado = "peso saludable"
elif imc <=29.9:
    estado = "Sobrepeso"
elif imc <=34.9:
    estado = "obesidad moderada"
elif imc <=39.9:
    estado = "obesidad severa"
else:
	estado = "obesidad severa"

print("su indice de masa corporral es: " +  str(imc) +  "y tu estado es: " +  estado)       

