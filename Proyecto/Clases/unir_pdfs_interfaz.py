import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def select_input_folder():
    folder_path = filedialog.askdirectory()
    input_folder_var.set(folder_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    output_file_var.set(file_path)

def merge_pdfs():
    input_folder = input_folder_var.get()
    output_file = output_file_var.get()

    if not os.path.isdir(input_folder):
        messagebox.showerror("Error", "La ruta de la carpeta de entrada no es válida.")
        return

    if not output_file:
        messagebox.showerror("Error", "La ruta del archivo de salida no es válida.")
        return

    pdf_merger = PdfMerger()
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    pdf_files.sort()

    for pdf in pdf_files:
        pdf_path = os.path.join(input_folder, pdf)
        pdf_merger.append(pdf_path)

    with open(output_file, 'wb') as f_out:
        pdf_merger.write(f_out)

    messagebox.showinfo("Éxito", f"Archivos PDF combinados y guardados en {output_file}")

# Configurar la ventana principal
root = tk.Tk()
root.title("Coprocom combinador de PDFs")
root.iconbitmap("C:\\Users\\edgar\\Downloads\\unnamed.ico")  # Cambia esto por la ruta de tu archivo .ico

input_folder_var = tk.StringVar()
output_file_var = tk.StringVar()

# Crear y organizar widgets
tk.Label(root, text="Ruta de la carpeta con archivos PDF:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Entry(root, textvariable=input_folder_var, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Seleccionar carpeta", command=select_input_folder).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Ruta y nombre del archivo combinado:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
tk.Entry(root, textvariable=output_file_var, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Seleccionar archivo", command=select_output_file).grid(row=1, column=2, padx=10, pady=5)

tk.Button(root, text="Combinar PDFs", command=merge_pdfs).grid(row=2, column=0, columnspan=3, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()

