# Ejercicio 4
while True:
    try:
        edad = int(input("Digite su edad: "))
        break  # Salir del bucle si se ingresó un float válido
    except ValueError:
        print("Error: El valor ingresado no es un número entero. Intente nuevamente.")
print("El género ingresado es:", edad)

opciones_validas = ["FEMENINO", "MASCULINO", "HOMBRE", "MUJER"]
while True:
    valor = input("Ingrese su género (Femenino/Masculino/Hombre/Mujer): ")
    valor = valor.upper()
    if valor in opciones_validas:
        break  # Salir del bucle si se ingresó un valor válido
    else:
        print("Error: sexo no válido. Intente nuevamente.")

print("El género ingresado es:", valor)

valorF=["FEMENINO", "MUJER"]
valorM=["MASCULINO", "HOMBRE"]

if valor in valorM and edad>65:
    print("Usted puede pensionarse")
elif valor in valorF and edad>62:
    print("Usted puede pensionarse")
else:
    print("Usted no tiene edad para pensionarse, vaya y trabaja")
