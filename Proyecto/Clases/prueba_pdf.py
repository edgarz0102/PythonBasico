import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import openpyxl
from openpyxl import Workbook

def add_page_numbers(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawString(10, 10, f"{str(i+1).zfill(5)}")
        can.save()

        packet.seek(0)
        watermark = PdfReader(packet).pages[0]

        page.merge_page(watermark)
        writer.add_page(page)

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

def merge_pdfs(input_folder, output_file, excel_path):
    pdf_writer = PdfWriter()
    current_page = 1

    wb = Workbook()
    ws = wb.active
    ws.append(["Nombre", "Folio"])

    for root, _, files in os.walk(input_folder):
        for file in sorted(files):
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                pdf_reader = PdfReader(file_path)
                num_pages = len(pdf_reader.pages)
                
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)
                
                if num_pages == 1:
                    folio = f"{str(current_page).zfill(5)}"
                else:
                    folio = f"{str(current_page).zfill(5)}-{str(current_page + num_pages - 1).zfill(5)}"
                
                ws.append([file, folio])
                current_page += num_pages
    
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

    add_page_numbers(output_file, output_file)
    wb.save(excel_path)

if __name__ == "__main__":
    input_folder = input("Enter the folder path containing PDF files: ")
    output_folder = input("Enter the folder path to save the combined PDF: ")
    output_filename = input("Enter the name for the combined PDF (without extension): ")
    excel_filename = input("Enter the name for the Excel file (without extension): ")

    output_file = os.path.join(output_folder, f"{output_filename}.pdf")
    excel_path = os.path.join(output_folder, f"{excel_filename}.xlsx")
    
    merge_pdfs(input_folder, output_file, excel_path)
    print(f"Combined PDF with page numbers saved as {output_file}")
    print(f"Excel file with file names and folios saved as {excel_path}")


