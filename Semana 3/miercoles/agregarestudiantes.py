class estudiantes:
    def __init__(self):
        self.clase = []
        self.clase1 = []

    def agregar(self):
        datos=[]
        while True:
            respuesta = input("¿Desea agregar un estudiante nuevo a la clase? (sí/no): ")
            if respuesta.lower() == "si":
                nombre = input("Nombre del estudiante: ")
                apellido = input("Apellido: ")
                edad = int(input("Edad: "))
                email = input("Email: ")
                fecha_nacimiento = input("Fecha de nacimiento: ")
                direccion = input("Dirección: ")
                provincia = input("Provincia: ")
                canton = input("Canton: ")
                distrito = input("Distrito: ")

                datos.append(nombre)
                datos.append(apellido)
                datos.append(edad)
                datos.append(email)                
                datos.append(fecha_nacimiento)
                datos.append(direccion)
                datos.append(provincia)
                datos.append(canton)
                datos.append(distrito)
                self.clase1.append(datos)

                estudiante = {
                    "Nombre": nombre,
                    "Apellido": apellido,
                    "Edad": edad,
                    "Email": email,
                    "Fecha Nacimiento": fecha_nacimiento,
                    "Direccion": direccion,
                    "Provincia": provincia,
                    "Canton": canton,
                    "Distrito": distrito
                }
                self.clase.append(estudiante)
            elif respuesta.lower() == "no":
                break
            else:
                print("Por favor, responda 'sí' o 'no'.")
        return self.clase1

    def cantidad(self):
        cantidad= len(self.clase)
        print("Usted agregó", cantidad, "estudiantes.")
        print(self.clase)
        print(self.clase1)


estudiantes = estudiantes()

g = estudiantes.agregar()
print( g )

estudiantes.cantidad()
