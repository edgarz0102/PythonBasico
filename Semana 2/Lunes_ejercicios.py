#triple comillas no da error
#Otra forma de concatenar es con corchetes, declarando con una f al inicio,"""" [}

capital=100000
inversion1=70000
inversion2=capital-inversion1
ganancia=inversion1*0.05+inversion2*0.1
print(ganancia)
print("La ganancia del inversionista es: ", ganancia)

#Ejercicio 2
monto_compra = float(input("Digite el valor 1: "))
descuento1 = float(input("Digite el valor 2: "))
base_imponible = monto_compra-descuento1
monto_1 = base_imponible*(1.13)
monto_2 = monto_compra*1.13-descuento1

if monto_1>monto_2:
    print("El método que genera un mayor beneficio es primero impuesto, después descuento, con total de ", monto_2)
else:
    print("El método que genera un mayor beneficio es primero descuento, después impuesto, con total de ", monto_1)

#Ejercio 3
valor_1 = float(input("Digite el valor 1: "))
valor_2 = float(input("Digite el valor 2: "))

if valor_1>valor_2:
    print("El número con mayor valor es", valor_1)
elif valor_2>valor_1:
    print("El número con yor valor es", valor_2)   
else:
    print("Los números son iguales")
# Ejercicio 4
while True:
    try:
        valor = float(input("Digite el valor de la compra: "))
        break  # Salir del bucle si se ingresó un float válido
    except ValueError:
        print("Error: El valor ingresado no es un número. Intente nuevamente.")

while True:
    try:
        pdescuento = float(input("Digite el porcentaje de descuento de la compra (1-100): "))
        if valor >= 1 and valor <= 100:
            break  # Salir del bucle si se ingresó un float válido en el rango
        else:
            print("Error: El valor debe estar entre 1 y 100. Intente nuevamente.")
    except ValueError:
        print("Error: El valor ingresado no es un número decimal. Intente nuevamente.")

while True:
    try:
        pimpuesto = float(input("Digite el valor del impuesto (entero): "))
        break  # Salir del bucle si se ingresó un float válido
    except ValueError:
        print("Error: El valor ingresado no es un número. Intente nuevamente.")
pdescuento=pdescuento/100
pimpuesto=pimpuesto/100
descuento=valor*pdescuento
base_imponible=valor*(1-pdescuento)
impuesto=base_imponible*pimpuesto
total_a_pagar=base_imponible*(1-pimpuesto)

print("El valor del original del articulo es: ", valor)
print("El descuento aplicado es: ", descuento, "siendo el porcentaje de ", pdescuento)
print("El impuesto aplicado es: ", impuesto, "siendo el porcentaje de ", pimpuesto)
print("El total a pagar es de ", total_a_pagar, " unidades monetarias ")

# Ejercicio 5
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