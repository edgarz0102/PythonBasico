import os
from PyPDF2 import PdfMerger

def get_folder_path(prompt):
    folder_path = input(prompt)
    while not os.path.isdir(folder_path):
        print("La ruta proporcionada no es válida. Inténtalo de nuevo.")
        folder_path = input(prompt)
    return folder_path

def get_save_path(prompt):
    save_path = input(prompt)
    save_folder = os.path.dirname(save_path)
    while not os.path.isdir(save_folder):
        print("La ruta de guardado proporcionada no es válida. Inténtalo de nuevo.")
        save_path = input(prompt)
        save_folder = os.path.dirname(save_path)
    return save_path

def merge_pdfs(input_folder, output_file):
    pdf_merger = PdfMerger()
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    pdf_files.sort()

    for pdf in pdf_files:
        pdf_path = os.path.join(input_folder, pdf)
        pdf_merger.append(pdf_path)

    with open(output_file, 'wb') as f_out:
        pdf_merger.write(f_out)

if __name__ == "__main__":
    input_folder = get_folder_path("Ingresa la ruta de la carpeta con archivos PDF: ")
    output_folder = get_folder_path("Ingresa la ruta donde se guardará el archivo combinado: ")
    output_filename = input("Ingresa el nombre del archivo combinado (sin extensión): ") + ".pdf"
    output_file = os.path.join(output_folder, output_filename)

    merge_pdfs(input_folder, output_file)
    print(f"Archivos PDF combinados y guardados en {output_file}")
