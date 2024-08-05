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

