#Escriba un programa que lea un número y
# le diga al usuario si es mayor o menor a 5.

#Escriba un pseudocódigo(programa, algoritmo) que realice lo siguiente:
# Pida a un usuario que ingrese un número. 
#Si el número está entre 0 y 10, escribe la palabra azul. 
#Si el número está entre 11 y 20, escriba la palabra rojo. 
#Si el número está entre 21 y 30, escribe la palabra verde. 
#Si es cualquier otro número, escriba que no es una opción 
#de color correcta.

#crear un programa que recorra los numero del 1 al 100, 
#pero que solo imprima los numeros o multiplos de 5

#optativo
#Cree un programa que reciba un número del 1 al 100 y 
#sume en una variable todos los números desde el 1
#hasta el número ingresado por el usuario e imprima el resultado.

numero = int(input("Ingrese un número: "))
if numero >5 :
    print("Número es mayor que 5")
elif numero < 5:
    print("Número es menor que 5")
else:
    print("El número es 5")

numero = int(input("Ingrese un número: "))

if numero >= 0 and numero <= 10:
    print("Azul")
elif numero >= 11 and numero <= 20:
    print("Rojo")
elif numero >= 21 and numero <= 30:
    print("Verde")
else:
    print("No es una opción de color correcta")


numero = int(input("Ingrese un número: "))
for i in range(numero+1):
    if i%5==0:
        print(i)
    else:
        True

numero = int(input("Ingrese un número: "))
suma=(numero*(numero+1))/2
print("La suma del 1 al ", numero, " es ", suma)

