class profesoresc:
    def __init__(self):
        self.clase = []

    def verificartexto(self,mensaje):
        texto = None
        while not texto:
            texto = input(mensaje)
            if not texto:
                print("El campo no puede estar vacío, por favor digite un valor")
        return texto
    def verificarnumero(self,mensaje):
        while True:
            try:
                numero = int(input(mensaje))
                break
            except ValueError:
                print("Error: El valor ingresado no es un número. Intente nuevamente.")
        return numero

    def agregarprof(self):
        print("Digite la información del profesor")
        id_profesor = self.verificartexto("Digite el ID del profesor: ")
        nombre = self.verificartexto("Nombre: ")
        apellido = self.verificartexto("Apellido: ")
        edad = self.verificarnumero("Edad: ")
        email = self.verificartexto("Email: ")


        profesores = {
            "Cedula":id_profesor,
            "Nombre": nombre,
            "Apellido": apellido,
            "Edad": edad,
            "Email": email
        }

        self.clase.append(profesores)

        return self.clase
    

