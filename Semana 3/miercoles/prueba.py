class Estudiantes:
    def __init__(self):
        self.clase = []
        self.clase1 = []

    def agregar_estudiante(self):
        while True:
            respuesta = input("¿Desea agregar un estudiante nuevo a la clase? (sí/no): ")

            if respuesta.lower() == "sí":
                datos = []
                nombre = input("Nombre del estudiante: ")
                apellido = input("Apellido del estudiante: ")
                edad = int(input("Edad del estudiante: "))
                correo = input("Correo del estudiante: ")
                email = input("Email del estudiante: ")
                fecha_nacimiento = input("Fecha de nacimiento del estudiante: ")
                direccion = input("Dirección del estudiante: ")
                provincia = input("Provincia del estudiante: ")
                canton = input("Cantón del estudiante: ")
                distrito = input("Distrito del estudiante: ")

                datos.append(nombre)
                datos.append(apellido)
                datos.append(edad)
                datos.append(correo)
                datos.append(email)
                datos.append(fecha_nacimiento)
                datos.append(direccion)
                datos.append(provincia)
                datos.append(canton)
                datos.append(distrito)
                self.clase1.append(datos)
                self.clase.append(datos)
            elif respuesta.lower() == "no":
                break
            else:
                print("Por favor, responda 'sí' o 'no'.")

    def imprimir_cantidad_estudiantes(self):
        cantidad_estudiantes = len(self.clase)
        print("Usted agregó", cantidad_estudiantes, "estudiantes.")
        print("Datos de los estudiantes:", self.clase)
        print("Datos de clase1:", self.clase1)


# Ejemplo de uso
estudiantes = Estudiantes()
estudiantes.agregar_estudiante()
estudiantes.imprimir_cantidad_estudiantes()

