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
