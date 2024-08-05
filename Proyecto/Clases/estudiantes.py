class estudiantes:
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

    def agregar(self):
        print("Bienvenido al módulo de estudiantes")
        while True:
            respuesta = input("¿Desea agregar un estudiante nuevo a la clase? (sí/no): ")
            if respuesta.lower() == "si" or respuesta.lower() == "sí"  :
                
                id_estudiante = self.verificartexto("Digite el ID del estudiante: ")
                nombre = self.verificartexto("Nombre: ")
                apellido = self.verificartexto("Apellido: ")
                edad = self.verificarnumero("Edad: ")
                email = self.verificartexto("Email: ")

                estudiante = {
                    "Cedula": id_estudiante,
                    "Nombre": nombre,
                    "Apellido": apellido,
                    "Edad": edad,
                    "Email": email
                }
                self.clase.append(estudiante)
            elif respuesta.lower() == "no":
                break
            else:
                print("Por favor, responda 'sí' o 'no'.")
        return self.clase
    def cantidad(self):
        cantidad= len(self.clase)
        print("Usted agregó", cantidad, "estudiantes.")




