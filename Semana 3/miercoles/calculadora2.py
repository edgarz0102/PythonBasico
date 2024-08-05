class calculadora:
    def suma(self, a, b):
        return a + b
    def resta(self, a, b):
        return a - b
    def multiplicacion(self, a, b):
        return a * b
    def division(self, a, b):
        return a / b if b != 0 else "No se puede dividir por cero."
    def potencia(self, a, b):
        return a ** b
    def operar(self):
        while True:
            numero = int(input("Digite 1(suma), 2 (resta), 3 (multi), 4 (div), 5(potencia). 0 (salir): "))
            if numero==0:
                break
            a = float(input("Digite el primer número: "))
            b = float(input("Digite el segundo número: "))
            if numero==1:
                print("Suma:", self.suma(a, b))
            elif numero==2:
                print("Resta:", self.resta(a, b))
            elif numero==3:
                print("Multiplicación:", self.multiplicacion(a, b))
            elif numero==4:
                print("División:", self.division(a, b))
            elif numero==5:
                print("Potencia:", self.potencia(a, b))
            else:
                break
    def imprimir(self):
        print("Hola mundo")
calculadora = calculadora()
calculadora.operar()
calculadora.imprimir()
