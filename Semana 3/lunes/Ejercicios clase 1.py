#Ejercicio 1
#Realizar un algoritmo que visualice la siguiente progresión aritmética:
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def pot(a,b):
    return a**b
    

while True:
    numero = int(input("Digite 1(suma), 2 (resta), 3 (multi), 4 (div), 5(potencia). 0 (salir): "))
    resultado=0
    if numero==0:
        break
    a = float(input("Digite el primer número: "))
    b = float(input("Digite el segundo número: "))
    if numero==1:
        resultado=suma(a,b)
        print(resultado)
    elif numero==2:
        resultado=resta(a,b)
        print(resultado)
    elif numero==3:
        resultado=multi(a,b)
        print(resultado)
    elif numero==4:
        resultado=div(a,b)
        print(resultado)
    elif numero==5:
        resultado=pot(a,b)
        print(resultado)
    else:
        break

    #Ejercicio2
def fibonacci(n):
    lista = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return lista

    while len(lista) < n:
        fibo_num = lista[-1] + lista[-2]
        lista.append(fibo_num)
    return lista
n = int(input("Ingrese la cabtidad de elementos de la serie de Fibonacci que desea imprimir: "))

fibonacci_pedir = fibonacci(n)
print(fibonacci_pedir)

#Ejercicio 3
def esparimpar(fin):
    rango=range(1, fin+1)
    pares=[]
    impares=[]
    for i in rango:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

fin=int(input("Ingrese el número final del rango: "))
pares, impares = esparimpar(fin)
print("Los pares son: ",pares)
print("Los impares son: ",impares)

#Ejercicio 4
def serie(a,b,c):
    lista=[]
    for i in range(1,a+1):
        an=c+b*(i-1)
        lista.append(an)
    return lista

a = int(input("Ingrese la longitud de terminos de la serie: "))
b = int(input("Ingrese ""d"" de la serie aritmeética: "))
c = int(input("Ingrese el primer término de la serie aritmética: "))
k=serie(a,b,c)
print(k)