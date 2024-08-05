class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "No se puede dividir por cero."
    def potencia(self, a, b):
        return a ** b
       
while True:
    calculadora = Calculadora()
    numero = int(input("Digite 1(suma), 2 (resta), 3 (multi), 4 (div), 5(potencia). 0 (salir): "))
    if numero==0:
        break
    a = float(input("Digite el primer número: "))
    b = float(input("Digite el segundo número: "))
    if numero==1:
        print("Suma:", calculadora.sumar(a, b))
    elif numero==2:
        print("Resta:", calculadora.restar(a, b))
    elif numero==3:
        print("Multiplicación:", calculadora.multiplicar(a, b))
    elif numero==4:
        print("División:", calculadora.dividir(a, b))
    elif numero==5:
        print("Potencia:", calculadora.potencia(a, b))
    else:
        break