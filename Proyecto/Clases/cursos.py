class cursosc:
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

    def agregarcurso(self):
        id_curso = self.verificartexto("Digite el ID del curso: ")
        nombre = self.verificartexto("Nombre del curso: ")
        creditos = self.verificarnumero("Digite la cantidad de créditos del curso: ")

        cursos = {
            "Siglas":id_curso,
            "Nombre": nombre,
            "Creditos": creditos
        }

        self.clase.append(cursos)

        return self.clase
