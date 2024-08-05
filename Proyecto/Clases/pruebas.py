import openpyxl

# Obtener la longitud de la serie
n = int(input("Ingresa la longitud de la serie: "))

# Crear un nuevo libro de Excel y seleccionar la hoja activa
workbook = openpyxl.Workbook()
sheet = workbook.active

# Agregar encabezado a la columna
sheet["A1"] = "recordID"

# Generar la serie de números y guardarlos en la columna
for i in range(1, n+1):
    sheet.cell(row=i+1, column=1, value=i)

# Guardar el libro de Excel
workbook.save("serie.xlsx")
print("Archivo 'serie.xlsx' creado exitosamente.")