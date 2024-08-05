from cursos import cursosc
from estudiantes import estudiantes
from profesores import profesoresc

class App:
    def __init__(self):
        self.bd = []
        self.cursos_prueba=[]
        self.estudiantes_prueba=[]
        self.diccionario = {}
    
    def almacenar(self):
        print("Bienvenido al sistema")
        self.cursos_prueba=[]
        contador=0
        contador2=0
        while True:
            respuesta = input("¿Desea agregar un nuevo curso al sistema? (sí/no): ")
            if respuesta.lower() == "si" or respuesta.lower() == "sí":
                cursoalm = cursosc()
                curso = cursoalm.agregarcurso()
                self.bd.append(curso)

                profalm = profesoresc()
                prof = profalm.agregarprof()
                self.bd.append(prof)
                
                estudiantesalm = estudiantes()
                estud = estudiantesalm.agregar()
                self.bd.append(estud)
                self.estudiantes_prueba.append(estud)


                estudiantesalm.cantidad()

                z=self.bd[contador][0]['Nombre']
                self.diccionario=self.estudiantes_prueba[0][contador2]
                self.diccionario["Curso"]= z
                contador=+3
                contador2=+1
                self.cursos_prueba.append(self.diccionario)


            elif respuesta.lower() == "no":
                break
            else:
                print("Por favor, responda 'sí' o 'no'.")

        return self.bd, self.cursos_prueba, self.estudiantes_prueba, self.diccionario

app = App()
h = app.almacenar()
print(h[0])
print(h[1])
print(h[2])
print(h[3])
